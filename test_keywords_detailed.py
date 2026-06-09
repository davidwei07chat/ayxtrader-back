#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
详细诊断脚本 - 搜索特定关键词在采集数据中的出现情况
"""

import sys
import os
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from aiyxdata_tradar.core import load_config
from aiyxdata_tradar.crawler import DataFetcher
from aiyxdata_tradar.context import AppContext


def search_keywords_in_data():
    """搜索关键词在采集数据中的出现情况"""

    print("=" * 80)
    print("TrendRadar 关键词诊断 - 详细搜索")
    print("=" * 80)

    # 加载配置
    print("\n[1] 加载配置...")
    config = load_config()
    ctx = AppContext(config)
    print(f"✓ 配置加载完成")

    # 初始化数据获取器
    print("\n[2] 初始化数据获取器...")
    proxy_url = config.get("DEFAULT_PROXY") if config.get("USE_PROXY") else None
    data_fetcher = DataFetcher(proxy_url)
    print(f"✓ 数据获取器初始化完成")

    # 获取平台列表
    print("\n[3] 获取平台列表...")
    ids = []
    for platform in ctx.platforms:
        if "name" in platform:
            ids.append((platform["id"], platform["name"]))
        else:
            ids.append(platform["id"])

    # 执行采集
    print("\n[4] 执行数据采集...")
    request_interval = config.get("REQUEST_INTERVAL", 500)
    results, id_to_name, failed_ids = data_fetcher.crawl_websites(ids, request_interval)

    print(f"✓ 采集完成")
    print(f"  - 成功平台: {len(results)}")

    # 定义搜索关键词
    search_keywords = ["上海本地生活", "OPC", "上海", "本地生活"]

    print("\n" + "=" * 80)
    print("搜索结果")
    print("=" * 80)

    # 对每个关键词进行搜索
    for keyword in search_keywords:
        print(f"\n【搜索关键词】: {keyword}")
        print("-" * 80)

        found_count = 0
        results_by_source = {}

        # 在所有采集数据中搜索
        for source_id, titles in results.items():
            source_name = id_to_name.get(source_id, source_id)
            matching_titles = []

            for title in titles.keys():
                if keyword.lower() in title.lower():
                    matching_titles.append(title)
                    found_count += 1

            if matching_titles:
                results_by_source[source_name] = matching_titles

        if found_count > 0:
            print(f"✓ 找到 {found_count} 条相关新闻\n")
            for source_name, titles in results_by_source.items():
                print(f"  【{source_name}】({len(titles)} 条)")
                for i, title in enumerate(titles[:5], 1):
                    print(f"    {i}. {title}")
                if len(titles) > 5:
                    print(f"    ... 还有 {len(titles) - 5} 条")
        else:
            print(f"✗ 未找到任何相关新闻")

    # 显示所有采集到的新闻统计
    print("\n" + "=" * 80)
    print("采集数据统计")
    print("=" * 80)

    total_news = 0
    for source_id, titles in results.items():
        source_name = id_to_name.get(source_id, source_id)
        news_count = len(titles)
        total_news += news_count
        print(f"  {source_name}: {news_count} 条新闻")

    print(f"\n  总计: {total_news} 条新闻")

    # 显示所有新闻标题（用于完整参考）
    print("\n" + "=" * 80)
    print("所有采集到的新闻标题")
    print("=" * 80)

    for source_id, titles in results.items():
        source_name = id_to_name.get(source_id, source_id)
        print(f"\n【{source_name}】")
        for i, title in enumerate(titles.keys(), 1):
            print(f"  {i}. {title}")

    print("\n" + "=" * 80)
    print("诊断完成！")
    print("=" * 80)


if __name__ == "__main__":
    try:
        search_keywords_in_data()
    except Exception as e:
        print(f"\n❌ 诊断出错: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
