#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
RSS 数据源关键词测试脚本
测试 RSS 源中是否能采集到"上海本地生活"和"OPC"相关内容
"""

import sys
from pathlib import Path

# 添加项目路径
sys.path.insert(0, str(Path(__file__).parent))

from aiyxdata_tradar.context import AppContext
from aiyxdata_tradar.crawler.rss import RSSFetcher, RSSFeedConfig
from aiyxdata_tradar.core.analyzer import count_word_frequency
from aiyxdata_tradar.core import load_config
from aiyxdata_tradar.utils.time import DEFAULT_TIMEZONE


def main():
    # 加载配置
    config = load_config()

    # 初始化上下文
    ctx = AppContext(config)

    # 获取 RSS 配置
    rss_feeds = ctx.rss_feeds
    if not rss_feeds:
        print("[RSS] 未配置任何 RSS 源")
        return

    print(f"[RSS] 找到 {len(rss_feeds)} 个 RSS 源配置")

    # 构建 RSSFeedConfig 对象列表（按照 __main__.py 的方式）
    feeds = []
    for feed_config in rss_feeds:
        max_age_days_raw = feed_config.get("max_age_days")
        max_age_days = None
        if max_age_days_raw is not None:
            try:
                max_age_days = int(max_age_days_raw)
                if max_age_days < 0:
                    max_age_days = None
            except (ValueError, TypeError):
                max_age_days = None

        feed = RSSFeedConfig(
            id=feed_config.get("id", ""),
            name=feed_config.get("name", ""),
            url=feed_config.get("url", ""),
            max_items=feed_config.get("max_items", 50),
            enabled=feed_config.get("enabled", True),
            max_age_days=max_age_days,
        )
        if feed.id and feed.url and feed.enabled:
            feeds.append(feed)
            print(f"  ✓ {feed.name} ({feed.id}): {feed.url}")

    if not feeds:
        print("[RSS] 没有启用的 RSS 源")
        return

    print(f"\n[RSS] 开始采集 {len(feeds)} 个启用的 RSS 源...")

    # 获取 RSS 配置
    rss_config = ctx.rss_config
    rss_proxy_url = rss_config.get("PROXY_URL", "") or ""
    timezone = ctx.config.get("TIMEZONE", DEFAULT_TIMEZONE)
    freshness_config = rss_config.get("FRESHNESS_FILTER", {})
    freshness_enabled = freshness_config.get("ENABLED", True)
    default_max_age_days = freshness_config.get("MAX_AGE_DAYS", 3)

    # 创建 RSS 抓取器
    fetcher = RSSFetcher(
        feeds=feeds,
        request_interval=rss_config.get("REQUEST_INTERVAL", 2000),
        timeout=rss_config.get("TIMEOUT", 15),
        use_proxy=rss_config.get("USE_PROXY", False),
        proxy_url=rss_proxy_url,
        timezone=timezone,
        freshness_enabled=freshness_enabled,
        default_max_age_days=default_max_age_days,
    )

    # 抓取数据
    rss_data = fetcher.fetch_all()

    if not rss_data or not rss_data.items:
        print("[RSS] 未采集到任何数据")
        return

    # 展平所有 RSS 项目
    all_items = []
    for feed_id, items in rss_data.items.items():
        all_items.extend(items)

    print(f"\n[RSS] 采集到 {len(all_items)} 条 RSS 项目")

    # 显示采集到的数据样本
    print("\n=== RSS 采集数据样本（前20条） ===")
    for i, item in enumerate(all_items[:20], 1):
        print(f"{i}. [{item.feed_name}] {item.title}")

    # 测试关键词匹配
    print("\n=== 关键词匹配测试 ===")

    # 创建测试词组
    test_keywords = [
        {
            "group_key": "shanghai_local_life",
            "display_name": "上海本地生活",
            "required": [],
            "normal": [{"word": "上海本地生活", "is_regex": False}],
            "filter": [],
            "max_count": 0,
            "tags": []
        },
        {
            "group_key": "opc",
            "display_name": "OPC",
            "required": [],
            "normal": [{"word": "OPC", "is_regex": False}],
            "filter": [],
            "max_count": 0,
            "tags": []
        },
        {
            "group_key": "one_person_company",
            "display_name": "一人公司",
            "required": [],
            "normal": [{"word": "一人公司", "is_regex": False}],
            "filter": [],
            "max_count": 0,
            "tags": []
        }
    ]

    # 转换为新闻数据格式（results 字典格式）
    results = {}
    for item in all_items:
        feed_id = item.feed_id
        if feed_id not in results:
            results[feed_id] = {}

        results[feed_id][item.title] = {
            "title": item.title,
            "url": item.url,
            "publish_time": item.published_at,
        }

    # 执行关键词匹配
    for keyword in test_keywords:
        stats, total_new = count_word_frequency(
            results=results,
            word_groups=[keyword],
            filter_words=[],
            id_to_name=rss_data.id_to_name,
            quiet=True
        )

        count = len(stats)
        print(f"\n关键词: {keyword['display_name']}")
        print(f"  匹配条数: {count}")

        # 显示匹配的新闻
        if count > 0:
            for stat in stats:
                titles = stat.get('titles', [])
                if titles:
                    print(f"  匹配的新闻 ({len(titles)} 条):")
                    for i, title_item in enumerate(titles[:5], 1):  # 显示前5条
                        # title_item 可能是字典或字符串
                        if isinstance(title_item, dict):
                            title = title_item.get('title', 'N/A')
                            source = title_item.get('source_name', '')
                            print(f"    {i}. [{source}] {title}")
                        else:
                            print(f"    {i}. {title_item}")
                else:
                    print(f"  未找到匹配的新闻标题")

    # 显示所有 RSS 源的数据统计
    print("\n=== RSS 源数据统计 ===")
    source_stats = {}
    for item in all_items:
        if item.feed_name not in source_stats:
            source_stats[item.feed_name] = 0
        source_stats[item.feed_name] += 1

    for source, count in sorted(source_stats.items(), key=lambda x: x[1], reverse=True):
        print(f"  {source}: {count} 条")

    print(f"\n总计: {len(all_items)} 条")


if __name__ == "__main__":
    main()
