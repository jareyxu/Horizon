"""Pre-process long-form content before normal scoring and enrichment."""

from __future__ import annotations

import asyncio

from .client import AIClient
from ..models import ContentItem


class LongFormProcessor:
    """Create a bounded, whole-document digest from long podcast transcripts."""

    def __init__(
        self,
        ai_client: AIClient,
        *,
        chunk_chars: int = 6000,
        max_chunks: int = 6,
        concurrency: int = 2,
    ):
        self.client = ai_client
        self.chunk_chars = max(chunk_chars, 2000)
        self.max_chunks = max(max_chunks, 1)
        self.concurrency = max(concurrency, 1)

    async def process_batch(self, items: list[ContentItem]) -> None:
        targets = [
            item
            for item in items
            if item.metadata.get("source_variant") == "podcast"
            and len(item.content or "") > self.chunk_chars
        ]
        if not targets:
            return
        await asyncio.gather(*(self._process_item(item) for item in targets))

    async def _process_item(self, item: ContentItem) -> None:
        chunks = self._split(item.content or "")[: self.max_chunks]
        semaphore = asyncio.Semaphore(self.concurrency)

        async def summarize(index: int, chunk: str) -> tuple[int, str]:
            async with semaphore:
                response = await self.client.complete(
                    system=(
                        "你是播客研究助理。只根据提供的逐字稿片段提取事实、观点、"
                        "案例和可执行建议。使用简体中文，不要补充片段中没有的信息。"
                    ),
                    user=(
                        f"播客：{item.title}\n"
                        f"片段 {index + 1}/{len(chunks)}：\n{chunk}\n\n"
                        "请输出 4-8 条紧凑要点。"
                    ),
                )
                return index, response.strip()

        try:
            summaries = await asyncio.gather(
                *(summarize(index, chunk) for index, chunk in enumerate(chunks))
            )
        except Exception:
            item.metadata["longform_summarized"] = False
            return

        summaries.sort(key=lambda value: value[0])
        digest = "\n\n".join(
            f"### 逐字稿片段 {index + 1}\n{text}" for index, text in summaries if text
        )
        if digest:
            item.metadata["longform_original_chars"] = len(item.content or "")
            item.metadata["longform_chunk_count"] = len(chunks)
            item.metadata["longform_summarized"] = True
            item.content = digest

    def _split(self, text: str) -> list[str]:
        paragraphs = [part.strip() for part in text.split("\n\n") if part.strip()]
        chunks: list[str] = []
        current: list[str] = []
        current_len = 0
        for paragraph in paragraphs:
            if current and current_len + len(paragraph) + 2 > self.chunk_chars:
                chunks.append("\n\n".join(current))
                current = []
                current_len = 0
            if len(paragraph) > self.chunk_chars:
                if current:
                    chunks.append("\n\n".join(current))
                    current = []
                    current_len = 0
                chunks.extend(
                    paragraph[offset : offset + self.chunk_chars]
                    for offset in range(0, len(paragraph), self.chunk_chars)
                )
                continue
            current.append(paragraph)
            current_len += len(paragraph) + 2
        if current:
            chunks.append("\n\n".join(current))
        return chunks
