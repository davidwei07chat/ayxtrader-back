#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
小绿文 RSS 源诊断脚本
检查为什么只有标题，没有发布时间和作者
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from aiyxdata_tradar.core import load_config
from aiyxdata_tradar.crawler.rss import RSSFetcher, RSSFeedConfig
from aiyxdata_tradar.context import AppContext
from aiyxdata_tradar.utils.time import DEFAULT_TIMEZONE


def diagnose_gzh():
    """诊断小绿文 RSS 源"""

    print("=" * 80)
    print("小绿文 RSS 源诊断")
    print("=" * 80)

    # 加载配置
    print("\n[1] 加载配置...")
    config = load_config()
    ctx = AppContext(config)
    print(f"✓ 配置加载完成")

    # 获取小绿文源配置
    print("\n[2] 查找小绿文源配置...")
    rss_feeds = ctx.rss_feeds
    gzh_config = None

    for feed in rss_feeds:
        if feed.get("id") == "gzh":
            gzh_config = feed
            break

    if not gzh_config:
        print("✗ 未找到小绿文源配置")
        return

    print(f"✓ 找到小绿文源配置")
    print(f"  - ID: {gzh_config.get('id')}")
    print(f"  - 名称: {gzh_config.get('name')}")
    print(f"  - URL: {gzh_config.get('url')}")
    print(f"  - max_age_days: {gzh_config.get('max_age_days', '未设置（使用全局默认）')}")

    # 创建 RSSFeedConfig
    print("\n[3] 创建 RSS 源配置对象...")
    feed = RSSFeedConfig(
        id=gzh_config.get("id", ""),
        name=gzh_config.get("name", ""),
        url=gzh_config.get("url", ""),
        max_items=gzh_config.get("max_items", 50),
        enabled=gzh_config.get("enabled", True),
        max_age_days=gzh_config.get("max_age_days"),
    )
    print(f"✓ 配置对象创建完成")

    # 获取 RSS 配置
    rss_config = ctx.rss_config
    timezone = ctx.config.get("TIMEZONE", DEFAULT_TIMEZONE)
    freshness_config = rss_config.get("FRESHNESS_FILTER", {})
    freshness_enabled = freshness_config.get("ENABLED", True)
    default_max_age_days = freshness_config.get("MAX_AGE_DAYS", 3)

    print(f"\n[4] RSS 全局配置:")
    print(f"  - 新鲜度过滤启用: {freshness_enabled}")
    print(f"  - 全局 max_age_days: {default_max_age_days} 天")

    # 采集数据
    print("\n[5] 采集小绿文 RSS 源...")
    fetcher = RSSFetcher(
        feeds=[feed],
        request_interval=rss_config.get("REQUEST_INTERVAL", 2000),
        timeout=rss_config.get("TIMEOUT", 15),
        use_proxy=rss_config.get("USE_PROXY", False),
        proxy_url=rss_config.get("PROXY_URL", ""),
        timezone=timezone,
        freshness_enabled=freshness_enabled,
        default_max_age_days=default_max_age_days,
    )

    rss_data = fetcher.fetch_all()

    if not rss_data or not rss_data.items:
        print("✗ 未采集到任何数据")
        return

    # 展平所有项目
    all_items = []
    for feed_id, items in rss_data.items.items():
        all_items.extend(items)

    print(f"✓ 采集完成: {len(all_items)} 条文章")

    # 分析字段完整性
    print("\n[6] 字段完整性分析:")
    print(f"  - 总文章数: {len(all_items)}")

    if all_items:
        # 统计字段
        has_title = sum(1 for item in all_items if item.title)
        has_published_at = sum(1 for item in all_items if item.published_at)
        has_author = sum(1 for item in all_items if item.author)
        has_url = sum(1 for item in all_items if item.url)
        has_summary = sum(1 for item in all_items if item.summary)

        print(f"\n  字段覆盖率:")
        print(f"    标题 (title): {has_title}/{len(all_items)} ({100*has_title//len(all_items)}%)")
        print(f"    发布时间 (published_at): {has_published_at}/{len(all_items)} ({100*has_published_at//len(all_items)}%)")
        print(f"    作者 (author): {has_author}/{len(all_items)} ({100*has_author//len(all_items)}%)")
        print(f"    链接 (url): {has_url}/{len(all_items)} ({100*has_url//len(all_items)}%)")
        print(f"    摘要 (summary): {has_summary}/{len(all_items)} ({100*has_summary//len(all_items)}%)")

        # 显示前 5 条文章的详细信息
        print(f"\n  前 5 条文章的详细信息:")
        for i, item in enumerate(all_items[:5], 1):
            print(f"\n    {i}. 标题: {item.title}")
            print(f"       发布时间: {item.published_at if item.published_at else '(空)'}")
            print(f"       作者: {item.author if item.author else '(空)'}")
            print(f"       链接: {item.url if item.url else '(空)'}")
            print(f"       摘要: {item.summary[:50] if item.summary else '(空)'}...")

    # 与其他 RSS 源对比
    print("\n[7] 与其他 RSS 源字段对比:")
    print("  采集所有 RSS 源...")

    all_feeds = []
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
            all_feeds.append(feed)

    if all_feeds:
        fetcher_all = RSSFetcher(
            feeds=all_feeds,
            request_interval=rss_config.get("REQUEST_INTERVAL", 2000),
            timeout=rss_config.get("TIMEOUT", 15),
            use_proxy=rss_config.get("USE_PROXY", False),
            proxy_url=rss_config.get("PROXY_URL", ""),
            timezone=timezone,
            freshness_enabled=freshness_enabled,
            default_max_age_days=default_max_age_days,
        )

        rss_data_all = fetcher_all.fetch_all()

        if rss_data_all and rss_data_all.items:
            print(f"\n  各 RSS 源字段覆盖率:")
            print(f"  {'源名称':<20} {'总数':<6} {'发布时间':<12} {'作者':<12} {'链接':<12}")
            print(f"  {'-'*20} {'-'*6} {'-'*12} {'-'*12} {'-'*12}")

            for feed_id, items in rss_data_all.items.items():
                feed_name = rss_data_all.id_to_name.get(feed_id, feed_id)
                total = len(items)
                has_pub = sum(1 for item in items if item.published_at)
                has_auth = sum(1 for item in items if item.author)
                has_url = sum(1 for item in items if item.url)

                pub_pct = f"{100*has_pub//total}%" if total > 0 else "0%"
                auth_pct = f"{100*has_auth//total}%" if total > 0 else "0%"
                url_pct = f"{100*has_url//total}%" if total > 0 else "0%"

                marker = " ← 小绿文" if feed_name == "小绿文" else ""
                print(f"  {feed_name:<20} {total:<6} {pub_pct:<12} {auth_pct:<12} {url_pct:<12}{marker}")

    print("\n" + "=" * 80)
    print("诊断完成")
    print("=" * 80)


if __name__ == "__main__":
    try:
        diagnose_gzh()
    except Exception as e:
        print(f"\n❌ 诊断出错: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
