---
layout: default
title: Source Scrapers
---

# Source Scrapers

Horizon fetches content from multiple source types. All scrapers inherit from `BaseScraper`, share an async HTTP client, and implement a `fetch(since)` method that returns a list of `ContentItem` objects. Sources are fetched concurrently via `asyncio.gather`.

## AI HOT

**File**: `src/scrapers/aihot.py`

Reads the key-less public REST API at `/api/public/items`, supports cursor
pagination, filters by upstream score/category, and preserves both the original
article URL and the AI HOT Chinese reader permalink. Automated requests use an
identifiable project User-Agent.

## Follow Builders

**File**: `src/scrapers/follow_builders.py`

Reads the public X, podcast, and blog JSON feeds maintained by Follow Builders.
Each feed is isolated so a partial failure does not stop the others. The scraper
validates `generatedAt`, emits stable IDs, and compacts very long podcast
transcripts before the selected episode is summarized across chunks by the AI
pipeline.

## Hacker News

**File**: `src/scrapers/hackernews.py`

Uses the [Firebase HN API](https://hacker-news.firebaseio.com/v0):

- `GET /topstories.json` — fetches top story IDs
- `GET /item/{id}.json` — fetches story/comment details

Stories and their comments are fetched concurrently. For each story, the top 5 comments are included (deleted/dead comments excluded, HTML stripped, truncated at 500 chars).

**Config** (`sources.hackernews`):

```json
{
  "enabled": true,
  "fetch_top_stories": 30,
  "min_score": 100,
  "category": "tech"
}
```

- `fetch_top_stories` — number of top story IDs to fetch
- `min_score` — minimum HN points to include a story
- `category` — optional tag for balanced digest grouping

**Extracted data**: title, URL (falls back to HN discussion URL), author, score, comment count, top comment text, and category.

## GitHub

**File**: `src/scrapers/github.py`

Uses the [GitHub REST API](https://api.github.com):

- `GET /users/{username}/events/public` — user activity events
- `GET /repos/{owner}/{repo}/releases` — repository releases

Two source types are supported:

- **`user_events`** — tracks push, create, release, public, and watch events for a user
- **`repo_releases`** — tracks new releases for a specific repository

**Config** (`sources.github`, list of entries):

```json
{
  "type": "user_events",
  "username": "torvalds",
  "enabled": true,
  "category": "oss"
}
```

```json
{
  "type": "repo_releases",
  "owner": "golang",
  "repo": "go",
  "enabled": true,
  "category": "oss"
}
```

- `category` — optional tag for balanced digest grouping; set per source entry

**Authentication**: Set `GITHUB_TOKEN` in your environment for higher rate limits (5000 req/hr vs 60 without).

## RSS

**File**: `src/scrapers/rss.py`

Fetches any Atom/RSS feed using the `feedparser` library. Tries multiple date fields (`published`, `updated`, `created`) with fallback parsing.

**Config** (`sources.rss`, list of entries):

```json
{
  "name": "Simon Willison",
  "url": "https://simonwillison.net/atom/everything/",
  "enabled": true,
  "category": "ai-tools"
}
```

- `category` — optional tag for grouping (e.g., `"programming"`, `"microblog"`)

**Extracted data**: title, URL, author, content (from `summary`/`description`/`content` fields), feed name, category, and entry tags.

## Reddit

**File**: `src/scrapers/reddit.py`

Uses public, no-key Reddit endpoints. Subreddit listings and comments prefer `old.reddit.com` HTML because Reddit's unauthenticated JSON and RSS endpoints can intermittently block or fail:

- `GET https://old.reddit.com/r/{subreddit}/{sort}/` — subreddit posts
- `GET https://old.reddit.com/r/{subreddit}/comments/{post_id}/` — post comments
- `GET /r/{subreddit}/{sort}.json` — subreddit posts fallback
- `GET /user/{username}/submitted.json` — user submissions
- `GET /r/{subreddit}/comments/{post_id}.json` — post comments fallback
- `GET /r/{subreddit}/{sort}/.rss` — subreddit posts fallback when JSON is blocked

Subreddits and users are fetched concurrently. Comments are sorted by score, limited to the configured count, and exclude moderator-distinguished comments. Self-text is truncated at 1500 chars, comments at 500 chars.

**Config** (`sources.reddit`):

```json
{
  "enabled": true,
  "fetch_comments": 5,
  "subreddits": [
    {
      "subreddit": "MachineLearning",
      "sort": "hot",
      "fetch_limit": 25,
      "min_score": 10,
      "category": "ai-ml"
    }
  ],
  "users": [
    {
      "username": "spez",
      "sort": "new",
      "fetch_limit": 10,
      "category": "social"
    }
  ]
}
```

- `sort` — `hot`, `new`, `top`, or `rising` (subreddits); `hot` or `new` (users)
- `time_filter` — for `top`/`rising` sorts: `hour`, `day`, `week`, `month`, `year`, `all`
- `min_score` — minimum post score (subreddits only)
- `category` — optional tag for balanced digest grouping; set per subreddit or per user entry

**Rate limiting**: Detects HTTP 429 responses on JSON requests, reads the `Retry-After` header, waits, and retries once. Uses browser-like request headers for no-key public access.

**Extracted data**: title, URL, author, score, upvote ratio, comment count, subreddit, flair, self-text, top comments, and category.

## OpenBB

**File**: `src/scrapers/openbb.py`

Uses the [OpenBB Platform](https://www.openbb.co/platform) Python SDK via `obb.news.company()` to fetch company news for one or more ticker watchlists.

The scraper imports `openbb` lazily. If the optional dependency is not installed, Horizon logs a warning and skips the source instead of failing the whole run.

**Config** (`sources.openbb`):

```json
{
  "enabled": true,
  "watchlists": [
    {
      "name": "megacaps",
      "symbols": ["AAPL", "MSFT", "NVDA"],
      "enabled": true,
      "provider": "yfinance",
      "fetch_limit": 20,
      "category": "equities"
    }
  ]
}
```

- `watchlists` — each enabled watchlist triggers one `news.company()` call per run
- `provider` — OpenBB provider name for that watchlist
- `symbols` — tickers fetched together for the same provider
- `fetch_limit` — maximum rows requested from the provider
- `category` — optional metadata tag stored on each item

Behavior:

- Wraps the synchronous OpenBB SDK in `asyncio.to_thread` so the event loop stays responsive
- Deduplicates duplicate news across watchlists by article URL
- Skips malformed rows, rows without URL/title/date, and items older than the current time window
- Keeps fetching other watchlists if one provider call fails

**Credentials**: provider-specific secrets are resolved by the OpenBB SDK from its own environment variables or settings file. Horizon does not pass those values directly.

**Extracted data**: title, URL, author, published time, article body/excerpt, watchlist name, provider, category, and symbol list.

## Twitter

**Files**:

- `src/scrapers/twitter.py` — Apify
- `src/scrapers/twitter_playwright.py` — browser cookies
- `src/scrapers/twitter_rapidapi.py` — Twitter135 / RapidAPI

### Twitter135 / RapidAPI mode

Uses Twitter135's current read-only `/v2/UserTweets/` endpoint. The request
contains the account's public numeric `id` (`rest_id`) and `count`, plus
`X-RapidAPI-Key` and `X-RapidAPI-Host` headers. Horizon recursively normalizes
the timeline response so it tolerates the nested timeline variants returned by
the provider.

Quota controls:

1. One configured account produces at most one request per run.
2. `rapidapi_max_requests_per_run` caps the total even if more accounts are
   configured.
3. The scraper does not paginate and does not retry.
4. A failure for one account is isolated; HTTP 429 stops the remaining calls.
5. Tweet IDs are stable Horizon IDs, so existing storage deduplication removes
   posts seen on earlier runs.

Replies and retweets are excluded by default. Long Note Tweet text is preferred
over the truncated legacy text when present.

Use `scripts/resolve_twitter135_user.py` once to resolve usernames through
`/v2/UserByScreenName/`. Each supplied username consumes one request; the key is
read from `RAPIDAPI_KEY` and is never printed.

```json
{
  "enabled": true,
  "mode": "rapidapi",
  "fetch_limit": 10,
  "rapidapi_key_env": "RAPIDAPI_KEY",
  "rapidapi_host": "twitter135.p.rapidapi.com",
  "rapidapi_max_requests_per_run": 3,
  "rapidapi_users": [
    {"username": "karpathy", "rest_id": "33836629", "enabled": true}
  ]
}
```

**Extracted data**: full post text, canonical `x.com` URL, display name,
publish time, likes, reposts, replies, quotes, views, conversation ID, account
`rest_id`, source variant, and category.

### Apify mode

Uses the [Apify](https://apify.com) platform to bypass Twitter's anti-scraping measures. The actor `altimis~scweet` is called via the Apify REST API.

Flow:
1. POST to `/v2/acts/{actor_id}/runs` to trigger a run
2. Poll `/v2/actor-runs/{run_id}` until status is `SUCCEEDED` or a terminal failure
3. GET `/v2/datasets/{dataset_id}/items` to retrieve results

**Config** (`sources.twitter`):

```json
{
  "enabled": true,
  "users": ["karpathy", "ylecun"],
  "fetch_limit": 10,
  "fetch_reply_text": false,
  "max_replies_per_tweet": 3,
  "max_tweets_to_expand": 10,
  "reply_min_likes": 5,
  "actor_id": "altimis~scweet",
  "apify_token_env": "APIFY_TOKEN"
}
```

- `users` — Twitter screen names to monitor, without the `@` prefix
- `fetch_limit` — maximum tweets to fetch per run
- `category` — optional tag for balanced digest grouping (applies to all tweets from this source)
- `fetch_reply_text` — when `true`, a second Apify run fetches reply bodies for each important tweet and appends them under `--- Top Comments ---` for AI analysis
- `max_replies_per_tweet` — maximum reply lines per tweet (sorted by engagement score)
- `max_tweets_to_expand` — cap on reply expansion runs per pipeline cycle, to control Apify credit usage
- `reply_min_likes` — minimum likes required for a reply to be included
- `actor_id` — Apify actor ID (default: `altimis~scweet`)
- `apify_token_env` — environment variable name containing the Apify API token

**Authentication**: Set `APIFY_TOKEN` in your `.env`. Get a token at [console.apify.com](https://console.apify.com/account/integrations).

**Extracted data**: tweet text, URL, author, publish time, likes, retweets, replies, views, category, and (optionally) reply-thread text appended under `--- Top Comments ---`.
