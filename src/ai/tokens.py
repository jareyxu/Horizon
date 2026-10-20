"""Lightweight token usage tracker shared across AI clients.

This module keeps a simple in-memory counter of tokens used during a single
Horizon run, so the orchestrator can print a summary at the end.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from contextlib import contextmanager
from contextvars import ContextVar
from typing import Dict


@dataclass
class ProviderUsage:
    input_tokens: int = 0
    output_tokens: int = 0
    reported_calls: int = 0
    reasoning_tokens: int = 0
    reasoning_reported_calls: int = 0

    @property
    def total(self) -> int:
        return self.input_tokens + self.output_tokens


@dataclass
class TokenUsageSnapshot:
    total_input_tokens: int
    total_output_tokens: int
    per_provider: Dict[str, ProviderUsage] = field(default_factory=dict)
    per_stage: Dict[str, ProviderUsage] = field(default_factory=dict)

    def to_dict(self) -> dict:
        return asdict(self)

    @property
    def total_tokens(self) -> int:
        return self.total_input_tokens + self.total_output_tokens


_provider_usage: Dict[str, ProviderUsage] = {}
_stage_usage: Dict[str, ProviderUsage] = {}
_current_stage: ContextVar[str] = ContextVar("token_usage_stage", default="unattributed")


@contextmanager
def usage_stage(stage: str):
    """Attribute async child calls and retries without leaking across tasks."""
    token = _current_stage.set(stage)
    try:
        yield
    finally:
        _current_stage.reset(token)


def record_usage(provider: str, input_tokens: int = 0, output_tokens: int = 0, reasoning_tokens: int | None = None) -> None:
    """Accumulate token usage for a given provider.

    Args:
        provider: Provider identifier, e.g. "openai", "anthropic".
        input_tokens: Prompt / input tokens used.
        output_tokens: Completion / output tokens used.
    """
    if input_tokens <= 0 and output_tokens <= 0:
        return

    for usage in (
        _provider_usage.setdefault(provider, ProviderUsage()),
        _stage_usage.setdefault(_current_stage.get(), ProviderUsage()),
    ):
        usage.input_tokens += max(0, input_tokens)
        usage.output_tokens += max(0, output_tokens)
        usage.reported_calls += 1
        if isinstance(reasoning_tokens, int) and not isinstance(reasoning_tokens, bool):
            usage.reasoning_tokens += max(0, min(reasoning_tokens, output_tokens))
            usage.reasoning_reported_calls += 1


def get_usage_snapshot() -> TokenUsageSnapshot:
    """Return a snapshot of accumulated token usage."""
    total_in = sum(u.input_tokens for u in _provider_usage.values())
    total_out = sum(u.output_tokens for u in _provider_usage.values())
    return TokenUsageSnapshot(
        total_input_tokens=total_in,
        total_output_tokens=total_out,
        per_provider={key: ProviderUsage(**asdict(value)) for key, value in _provider_usage.items()},
        per_stage={key: ProviderUsage(**asdict(value)) for key, value in _stage_usage.items()},
    )


def reset_usage() -> None:
    """Reset all accumulated usage (useful for tests)."""
    _provider_usage.clear()
    _stage_usage.clear()
