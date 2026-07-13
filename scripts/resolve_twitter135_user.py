"""Resolve X usernames to public rest_id values through Twitter135."""

from __future__ import annotations

import argparse
import json
import os
import sys

import httpx

from src.scrapers.twitter_rapidapi import TwitterRapidAPIScraper


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Resolve X usernames for Horizon's Twitter135 configuration."
    )
    parser.add_argument("usernames", nargs="+", help="X usernames, with or without @")
    parser.add_argument(
        "--key-env",
        default="RAPIDAPI_KEY",
        help="Environment variable containing the RapidAPI key",
    )
    parser.add_argument(
        "--host",
        default="twitter135.p.rapidapi.com",
        help="RapidAPI host",
    )
    args = parser.parse_args()

    api_key = os.environ.get(args.key_env)
    if not api_key:
        print(
            f"Missing API key in environment variable {args.key_env}", file=sys.stderr
        )
        return 2

    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": args.host,
    }
    resolved = []
    with httpx.Client(timeout=30.0) as client:
        for raw_username in args.usernames:
            username = raw_username.strip().lstrip("@")
            response = client.get(
                f"https://{args.host}/v2/UserByScreenName/",
                headers=headers,
                params={"username": username},
            )
            response.raise_for_status()
            rest_id = TwitterRapidAPIScraper.find_user_rest_id(
                response.json(), username
            )
            if not rest_id:
                print(f"Could not resolve @{username}", file=sys.stderr)
                return 1
            resolved.append(
                {
                    "username": username,
                    "rest_id": rest_id,
                    "enabled": True,
                    "category": "builders",
                }
            )

    print(json.dumps(resolved, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
