"""Daily summary generation — pure programmatic rendering."""

import re
from datetime import timezone
from html import escape
from typing import List

from ..models import ContentItem


_CJK = r"[\u4e00-\u9fff\u3400-\u4dbf]"
_ASCII = r"[A-Za-z0-9]"


def _pangu(text: str) -> str:
    """Insert a space between CJK and ASCII letters/digits (Pangu spacing)."""
    text = re.sub(rf"({_CJK})({_ASCII})", r"\1 \2", text)
    text = re.sub(rf"({_ASCII})({_CJK})", r"\1 \2", text)
    return text


LABELS = {
    "en": {
        "header": "Horizon Daily",
        "source": "Source",
        "background": "Background",
        "discussion": "Discussion",
        "references": "References",
        "tags": "Tags",
        "reader": "Chinese reading",
        "verification": "Verification",
        "tracked_x_archive": "Other tracked X posts",
        "follow_builders_archive": "Other Follow Builders stories",
        "archive_heading": "More tracked content",
        "archive_tabs_label": "More tracked content sources",
        "archive_intro": (
            "Fetched items that did not enter the main digest remain available here."
        ),
        "archive_empty": "No additional items from this source today.",
        "archive_content_empty": "Open the original link to read this item.",
        "archive_variant_x": "X post",
        "archive_variant_podcast": "Podcast",
        "archive_variant_blog": "Blog",
        "archive_title_translation": "Chinese title",
        "archive_summary_translation": "Chinese summary",
        "verification_states": {
            "corroborated": "corroborated by multiple sources",
            "original_checked": "original source checked",
            "original_reachable": "original source reachable",
            "unverified": "unverified",
        },
        "selected_items": "From {total} items, {selected} important content pieces were selected",
        "empty_analyzed": "Analyzed {total} items, but none met the importance threshold.",
        "empty_body": (
            "No significant developments today. This might indicate:\n"
            "- A quiet day in your tracked sources\n"
            "- The AI score threshold is too high\n"
            "- Your information sources need expansion\n\n"
            "Consider:\n"
            "1. Lowering the `ai_score_threshold` in config.json\n"
            "2. Adding more diverse information sources\n"
            "3. Checking if the AI model is working correctly\n"
        ),
    },
    "zh": {
        "header": "Horizon 每日速递",
        "source": "来源",
        "background": "背景",
        "discussion": "社区讨论",
        "references": "参考链接",
        "tags": "标签",
        "reader": "中文阅读",
        "verification": "核验",
        "tracked_x_archive": "其他追踪推文",
        "follow_builders_archive": "其他 Follow Builders 资讯",
        "archive_heading": "更多追踪内容",
        "archive_tabs_label": "更多追踪内容来源",
        "archive_intro": "以下内容已于今日成功抓取，但未进入上方主列表。",
        "archive_empty": "今天该来源没有其他未入选内容。",
        "archive_content_empty": "请打开原文链接查看完整内容。",
        "archive_variant_x": "X 动态",
        "archive_variant_podcast": "播客",
        "archive_variant_blog": "博客",
        "archive_title_translation": "中文标题",
        "archive_summary_translation": "中文摘要",
        "verification_states": {
            "corroborated": "多源印证",
            "original_checked": "已核对原文",
            "original_reachable": "原文可访问",
            "unverified": "待核验",
        },
        "selected_items": "从 {total} 条内容中筛选出 {selected} 条重要资讯。",
        "empty_analyzed": "已分析 {total} 条内容，但没有达到重要性阈值的条目。",
        "empty_body": (
            "今日暂无重要动态，可能原因：\n"
            "- 今天关注的信息源较平静\n"
            "- AI 评分阈值设置过高\n"
            "- 信息源种类有待扩充\n\n"
            "建议：\n"
            "1. 在 config.json 中降低 `ai_score_threshold`\n"
            "2. 添加更多多样化的信息源\n"
            "3. 检查 AI 模型是否正常工作\n"
        ),
    },
}


class DailySummarizer:
    """Generates daily Markdown summaries from pre-analyzed content items."""

    def __init__(self):
        pass

    async def generate_summary(
        self,
        items: List[ContentItem],
        date: str,
        total_fetched: int,
        language: str = "en",
    ) -> str:
        """Generate daily summary in Markdown format.

        Items are rendered in score-descending order (already sorted by orchestrator).

        Args:
            items: High-scoring content items (already enriched)
            date: Date string (YYYY-MM-DD)
            total_fetched: Total number of items fetched before filtering
            language: Output language, either "en" or "zh"

        Returns:
            str: Markdown formatted summary
        """
        labels = LABELS.get(language, LABELS["en"])

        if not items:
            return self._generate_empty_summary(date, total_fetched, labels)

        header = (
            f"# {labels['header']} - {date}\n\n"
            f"> {labels['selected_items'].format(total=total_fetched, selected=len(items))}\n\n"
            "---\n\n"
        )

        # TOC
        toc_entries = []
        for i, item in enumerate(items):
            _t = item.metadata.get(f"title_{language}") or item.title
            t = str(_t).replace("[", "(").replace("]", ")")
            if language == "zh":
                t = _pangu(t)
            score = item.ai_score or "?"
            toc_entries.append(f"{i + 1}. [{t}](#item-{i + 1}) \u2b50\ufe0f {score}/10")
        toc = "\n".join(toc_entries) + "\n\n---\n\n"

        parts = [
            self._format_item(item, labels, language, i + 1)
            for i, item in enumerate(items)
        ]

        return header + toc + "".join(parts)

    def generate_pages_archive_tabs(
        self,
        tracked_x_items: List[ContentItem],
        follow_builders_items: List[ContentItem],
        selected_ids: set[str],
        language: str = "en",
    ) -> str:
        """Render Pages-only tab panels for non-selected tracked content."""
        labels = LABELS.get(language, LABELS["en"])
        tracked_x = self._archive_items(
            tracked_x_items,
            selected_ids,
            lambda item: item.metadata.get("source_variant") == "twitter135_rapidapi",
        )
        follow_builders = self._archive_items(
            follow_builders_items,
            selected_ids,
            lambda item: item.source_type.value == "follow_builders",
        )
        if not tracked_x and not follow_builders:
            return ""

        parts = [
            '\n\n<hr class="archive-divider">\n',
            '<section class="archive-tabs" data-archive-tabs>\n',
            f"<h2>{escape(labels['archive_heading'])}</h2>\n",
            f'<p class="archive-intro">{escape(labels["archive_intro"])}</p>\n',
            (
                '<div class="archive-tablist" role="tablist" '
                f'aria-label="{escape(labels["archive_tabs_label"], quote=True)}" hidden>\n'
            ),
            self._archive_tab_button(
                "tracked-x",
                labels["tracked_x_archive"],
                len(tracked_x),
                selected=True,
            ),
            self._archive_tab_button(
                "follow-builders",
                labels["follow_builders_archive"],
                len(follow_builders),
                selected=False,
            ),
            "</div>\n",
            self._archive_panel(
                "tracked-x",
                labels["tracked_x_archive"],
                tracked_x,
                labels,
                language,
                archive_kind="twitter135",
            ),
            self._archive_panel(
                "follow-builders",
                labels["follow_builders_archive"],
                follow_builders,
                labels,
                language,
                archive_kind="follow_builders",
            ),
            "</section>\n",
        ]
        return "".join(parts)

    def generate_tracked_x_archive(
        self,
        items: List[ContentItem],
        selected_ids: set[str],
        language: str = "en",
    ) -> str:
        """Backward-compatible wrapper for the original Pages archive API."""
        return self.generate_pages_archive_tabs(
            items, [], selected_ids, language=language
        )

    @staticmethod
    def _archive_items(
        items: List[ContentItem], selected_ids: set[str], predicate
    ) -> List[ContentItem]:
        return sorted(
            (item for item in items if item.id not in selected_ids and predicate(item)),
            key=lambda item: item.published_at,
            reverse=True,
        )

    @staticmethod
    def _archive_tab_button(key: str, label: str, count: int, *, selected: bool) -> str:
        selected_text = "true" if selected else "false"
        tab_index = "0" if selected else "-1"
        return (
            f'<button type="button" role="tab" id="archive-tab-{key}" '
            f'aria-controls="archive-panel-{key}" aria-selected="{selected_text}" '
            f'tabindex="{tab_index}" data-archive-tab="{key}" data-count="{count}">'
            f'<span>{escape(label)}</span><span class="archive-tab-count">'
            f"{count}</span></button>\n"
        )

    def _archive_panel(
        self,
        key: str,
        title: str,
        items: List[ContentItem],
        labels: dict,
        language: str,
        *,
        archive_kind: str,
    ) -> str:
        parts = [
            f'<div class="archive-panel" role="tabpanel" id="archive-panel-{key}" '
            f'aria-labelledby="archive-tab-{key}" data-archive-panel="{key}">\n',
            f'<h3 class="archive-panel-title">{escape(title)}</h3>\n',
        ]
        if not items:
            parts.append(
                f'<p class="archive-empty">{escape(labels["archive_empty"])}</p>\n'
            )
        else:
            for item in items:
                parts.append(
                    self._format_archive_item_html(
                        item,
                        labels,
                        language,
                        archive_kind=archive_kind,
                    )
                )
        parts.append("</div>\n")
        return "".join(parts)

    def _format_archive_item_html(
        self,
        item: ContentItem,
        labels: dict,
        language: str,
        *,
        archive_kind: str,
    ) -> str:
        title = str(item.metadata.get(f"title_{language}") or item.title)
        title_translation = ""
        content_translation = ""
        if archive_kind == "twitter135":
            content = str(item.content or item.ai_summary or "").strip()
        else:
            if language == "zh":
                title = item.title
                title_translation = str(item.metadata.get("title_zh") or "").strip()
                content_translation = str(
                    item.metadata.get("summary_zh")
                    or item.metadata.get("detailed_summary_zh")
                    or ""
                ).strip()
            content = str(item.ai_summary or item.content or "").strip()
            if len(content) > 1200:
                content = content[:1197].rstrip() + "..."
        if language == "zh":
            title = _pangu(title)
            content = _pangu(content)
            title_translation = _pangu(title_translation)
            content_translation = _pangu(content_translation)

        score = item.ai_score if item.ai_score is not None else "?"
        score_tier = self._score_tier(item.ai_score)
        source_line = self._format_archive_source(
            item, labels, language, archive_kind=archive_kind
        )
        safe_content = escape(content or labels["archive_content_empty"]).replace(
            "\n", "<br>\n"
        )
        title_translation_html = ""
        content_translation_html = ""
        if title_translation and title_translation != title:
            title_translation_html = (
                '<p class="archive-item-translation archive-title-translation">'
                f"<span>{escape(labels['archive_title_translation'])}</span>"
                f"{escape(title_translation)}</p>\n"
            )
        if content_translation and content_translation != content:
            safe_translation = escape(content_translation).replace("\n", "<br>\n")
            content_translation_html = (
                '<p class="archive-item-translation">'
                f"<span>{escape(labels['archive_summary_translation'])}</span>"
                f"{safe_translation}</p>\n"
            )
        return (
            '<article class="archive-item">\n'
            '<div class="archive-item-heading">\n'
            f'<h3><a href="{escape(str(item.url), quote=True)}">{escape(title)}</a></h3>\n'
            f'<span class="score-badge" data-tier="{score_tier}" '
            f'aria-label="{escape(str(score), quote=True)} out of 10">{escape(str(score))}</span>\n'
            "</div>\n"
            f"{title_translation_html}"
            f'<p class="source-line">{escape(source_line)}</p>\n'
            f'<p class="archive-item-content">{safe_content}</p>\n'
            f"{content_translation_html}"
            "</article>\n"
        )

    def _format_archive_source(
        self,
        item: ContentItem,
        labels: dict,
        language: str,
        *,
        archive_kind: str,
    ) -> str:
        published = item.published_at.astimezone(timezone.utc)
        if archive_kind == "twitter135":
            username = str(
                item.metadata.get("rapidapi_account_username")
                or item.author
                or "unknown"
            ).lstrip("@")
            source = f"Twitter/X · @{username}"
        else:
            variant = str(item.metadata.get("source_variant") or "blog")
            variant_label = labels.get(f"archive_variant_{variant}", variant)
            source = f"Follow Builders · {variant_label} · {item.author or 'unknown'}"

        if language == "zh":
            source += f" · {published.month}月{published.day}日 {published:%H:%M} UTC"
        else:
            source += f" · {published:%Y-%m-%d %H:%M} UTC"
        if archive_kind == "twitter135" or item.metadata.get("source_variant") == "x":
            source += self._format_x_engagement(item, language)
        return source

    @staticmethod
    def _score_tier(score: float | None) -> str:
        if score is None or score < 5:
            return "low"
        if score < 7:
            return "mid"
        if score < 9:
            return "good"
        return "high"

    @staticmethod
    def _format_x_engagement(item: ContentItem, language: str) -> str:
        meta = item.metadata
        values = [
            ("喜欢" if language == "zh" else "likes", meta.get("favorite_count")),
            ("转发" if language == "zh" else "reposts", meta.get("retweet_count")),
            ("回复" if language == "zh" else "replies", meta.get("reply_count")),
            ("浏览" if language == "zh" else "views", meta.get("view_count")),
        ]
        rendered = [f"{label} {value}" for label, value in values if value is not None]
        return f" · {' · '.join(rendered)}" if rendered else ""

    def generate_webhook_overview(
        self,
        items: List[ContentItem],
        date: str,
        total_fetched: int,
        language: str = "en",
    ) -> str:
        """Generate a compact overview for multi-message webhook delivery."""
        labels = LABELS.get(language, LABELS["en"])
        if not items:
            return self._generate_empty_summary(date, total_fetched, labels)

        if language == "zh":
            header = (
                f"# {labels['header']} - {date}\n\n"
                f"> 从 {total_fetched} 条内容中筛选出 {len(items)} 条重要资讯。\n\n"
                "下面会按新闻逐条发送详情，你可以只看感兴趣的标题。\n\n"
            )
        else:
            header = (
                f"# {labels['header']} - {date}\n\n"
                f"> Selected {len(items)} important items from {total_fetched} fetched items.\n\n"
                "Details will be sent item by item so you can read only the topics you care about.\n\n"
            )

        entries = []
        for i, item in enumerate(items, start=1):
            title = (
                str(item.metadata.get(f"title_{language}") or item.title)
                .replace("[", "(")
                .replace("]", ")")
            )
            if language == "zh":
                title = _pangu(title)
            score = item.ai_score or "?"
            entries.append(f"{i}. [{title}]({item.url}) \u2b50\ufe0f {score}/10")

        return header + "\n".join(entries)

    def generate_webhook_item(
        self,
        item: ContentItem,
        language: str,
        index: int,
        total: int,
    ) -> str:
        """Generate one item message for multi-message webhook delivery."""
        labels = LABELS.get(language, LABELS["en"])
        prefix = (
            f"第 {index}/{total} 条\n\n"
            if language == "zh"
            else f"Item {index}/{total}\n\n"
        )
        return prefix + self._format_item(item, labels, language, index).rstrip("-\n ")

    def _format_item(
        self, item: ContentItem, labels: dict, language: str, index: int
    ) -> str:
        """Format a single ContentItem into Markdown."""
        _title = item.metadata.get(f"title_{language}") or item.title
        title = str(_title).replace("[", "(").replace("]", ")")
        url = str(item.url)
        score = item.ai_score or "?"
        meta = item.metadata

        summary = (
            meta.get(f"detailed_summary_{language}")
            or meta.get("detailed_summary")
            or item.ai_summary
            or ""
        )
        background = meta.get(f"background_{language}") or meta.get("background") or ""
        discussion = (
            meta.get(f"community_discussion_{language}")
            or meta.get("community_discussion")
            or ""
        )

        if language == "zh":
            title = _pangu(title)
            summary = _pangu(summary)
            background = _pangu(background)
            discussion = _pangu(discussion)

        # Source line with parts joined by " · ", link appended at end
        source_type = item.source_type.value
        source_parts = [source_type]
        if meta.get("subreddit"):
            source_parts.append(f"r/{meta['subreddit']}")
        if meta.get("feed_name"):
            source_parts.append(meta["feed_name"])
        else:
            source_parts.append(item.author or "unknown")
        if item.published_at:
            if language == "zh":
                source_parts.append(
                    f"{item.published_at.month}月{item.published_at.day}日 "
                    f"{item.published_at:%H:%M}"
                )
            else:
                day = item.published_at.strftime("%d").lstrip("0")
                source_parts.append(item.published_at.strftime(f"%b {day}, %H:%M"))
        source_line = " \u00b7 ".join(source_parts)  # ·

        discussion_url = meta.get("discussion_url")
        if discussion_url:
            discussion_url = str(discussion_url)
            if discussion_url != url:
                source_line += f" · [{labels['discussion']}]({discussion_url})"

        reader_url = meta.get("reader_url")
        if reader_url and str(reader_url) != url:
            source_line += f" · [{labels['reader']}]({reader_url})"

        source_count = int(meta.get("source_count") or 1)
        if source_count > 1:
            if language == "zh":
                source_line += f" · {source_count} 个来源"
            else:
                source_line += f" · {source_count} sources"

        lines = [
            f'<a id="item-{index}"></a>',
            f"## [{title}]({url}) \u2b50\ufe0f {score}/10",  # ⭐️
            "",
            summary,
            "",
            source_line,
        ]

        verification_status = str(meta.get("verification_status") or "")
        if verification_status:
            verification_text = labels["verification_states"].get(
                verification_status,
                verification_status,
            )
            lines.extend(["", f"**{labels['verification']}**: {verification_text}"])

        if background:
            lines.append("")
            lines.append(f"**{labels['background']}**: {background}")

        sources = meta.get("sources") or []
        if sources:
            items_html = "".join(
                f'<li><a href="{s["url"]}">{s["title"]}</a></li>\n' for s in sources
            )
            lines += [
                "",
                f"<details><summary>{labels['references']}</summary>\n<ul>\n{items_html}\n</ul>\n</details>",
            ]

        if discussion:
            lines.append("")
            lines.append(f"**{labels['discussion']}**: {discussion}")

        if item.ai_tags:
            tags_str = ", ".join([f"`#{t}`" for t in item.ai_tags])
            lines.append("")
            lines.append(f"**{labels['tags']}**: {tags_str}")

        lines.append("")
        lines.append("---")

        return "\n".join(lines) + "\n\n"

    def _generate_empty_summary(
        self, date: str, total_fetched: int, labels: dict
    ) -> str:
        """Generate summary when no high-scoring items were found."""
        return (
            f"# {labels['header']} - {date}\n\n"
            f"> {labels['empty_analyzed'].format(total=total_fetched)}\n\n"
            + labels["empty_body"]
        )
