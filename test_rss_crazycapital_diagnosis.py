#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
疯投圈 RSS 源诊断脚本
检查为什么只显示 1 篇文章
"""

import sys
from pathlib import Path
from datetime import datetime, timedelta

sys.path.insert(0, str(Path(__file__).parent))

from aiyxdata_tradar.core import load_config
from aiyxdata_tradar.crawler.rss import RSSFetcher, RSSFeedConfig
from aiyxdata_tradar.context import AppContext
from aiyxdata_tradar.utils.time import DEFAULT_TIMEZONE


def diagnose_crazycapital():
    """诊断疯投圈 RSS 源"""

    print("=" * 80)
    print("疯投圈 RSS 源诊断")
    print("=" * 80)

    # 加载配置
    print("\n[1] 加载配置...")
    config = load_config()
    ctx = AppContext(config)
    print(f"✓ 配置加载完成")

    # 获取疯投圈源配置
    print("\n[2] 查找疯投圈源配置...")
    rss_feeds = ctx.rss_feeds
    crazycapital_config = None

    for feed in rss_feeds:
        if feed.get("id") == "crazycapital":
            crazycapital_config = feed
            break

    if not crazycapital_config:
        print("✗ 未找到疯投圈源配置")
        return

    print(f"✓ 找到疯投圈源配置")
    print(f"  - ID: {crazycapital_config.get('id')}")
    print(f"  - 名称: {crazycapital_config.get('name')}")
    print(f"  - URL: {crazycapital_config.get('url')}")
    print(f"  - max_age_days: {crazycapital_config.get('max_age_days', '未设置（使用全局默认）')}")

    # 创建 RSSFeedConfig
    print("\n[3] 创建 RSS 源配置对象...")
    feed = RSSFeedConfig(
        id=crazycapital_config.get("id", ""),
        name=crazycapital_config.get("name", ""),
        url=crazycapital_config.get("url", ""),
        max_items=crazycapital_config.get("max_items", 50),
        enabled=crazycapital_config.get("enabled", True),
        max_age_days=crazycapital_config.get("max_age_days"),
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
    print(f"  - 时区: {timezone}")

    # 采集数据
    print("\n[5] 采集疯投圈 RSS 源...")
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

    # 分析数据
    print("\n[6] 数据分析:")
    print(f"  - 总文章数: {len(all_items)}")

    if all_items:
        # 按发布时间分析
        print(f"\n  发布时间分布:")
        now = datetime.now()
        time_ranges = [
            (1, "1 天内"),
            (3, "3 天内"),
            (5, "5 天内"),
            (7, "7 天内"),
            (30, "30 天内"),
            (999, "30 天以上"),
        ]

        prev_days = 0
        for days, label in time_ranges:
            count = 0
            for item in all_items:
                if item.published_at:
                    try:
                        pub_time = datetime.fromisoformat(item.published_at.replace("Z", "+00:00"))
                        age_days = (now - pub_time).days
                        if prev_days <= age_days < days:
                            count += 1
                    except:
                        pass

            print(f"    {label}: {count} 条")
            prev_days = days

        # 显示最新的几篇文章
        print(f"\n  最新的 5 篇文章:")
        for i, item in enumerate(all_items[:5], 1):
            print(f"    {i}. {item.title}")
            print(f"       发布时间: {item.published_at}")

    # 与其他 RSS 源对比
    print("\n[7] 与其他 RSS 源对比:")
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
            source_stats = {}
            for feed_id, items in rss_data_all.items.items():
                feed_name = rss_data_all.id_to_name.get(feed_id, feed_id)
                source_stats[feed_name] = len(items)

            print(f"\n  各 RSS 源采集数量:")
            for source, count in sorted(source_stats.items(), key=lambda x: x[1], reverse=True):
                marker = "← 疯投圈" if source == "疯投圈" else ""
                print(f"    {source}: {count} 条 {marker}")

    print("\n" + "=" * 80)
    print("诊断完成")
    print("=" * 80)


if __name__ == "__main__":
    try:
        diagnose_crazycapital()
    except Exception as e:
        print(f"\n❌ 诊断出错: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
