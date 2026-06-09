#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
强制执行采集任务测试脚本
测试"上海本地生活"和"OPC"两个词组的采集效果
"""

import sys
import os
from pathlib import Path

# 添加项目路径
sys.path.insert(0, str(Path(__file__).parent))

from aiyxdata_tradar.core import load_config
from aiyxdata_tradar.crawler import DataFetcher
from aiyxdata_tradar.core.analyzer import count_word_frequency
from aiyxdata_tradar.context import AppContext


def test_keywords():
    """强制执行采集任务，测试指定关键词"""

    print("=" * 70)
    print("TrendRadar 关键词采集测试")
    print("=" * 70)

    # 加载配置
    print("\n[1] 加载配置...")
    config = load_config()
    ctx = AppContext(config)
    print(f"✓ 配置加载完成")
    print(f"  - 时区: {config.get('TIMEZONE', 'Asia/Shanghai')}")
    print(f"  - 监控平台数: {len(ctx.platforms)}")

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
    print(f"✓ 平台列表: {[p.get('name', p['id']) if isinstance(p, dict) else p[1] for p in ids]}")

    # 执行采集
    print("\n[4] 执行数据采集...")
    request_interval = config.get("REQUEST_INTERVAL", 500)
    print(f"  请求间隔: {request_interval}ms")

    results, id_to_name, failed_ids = data_fetcher.crawl_websites(ids, request_interval)

    print(f"✓ 采集完成")
    print(f"  - 成功平台: {len(results)}")
    print(f"  - 失败平台: {failed_ids if failed_ids else '无'}")

    # 统计采集数据
    total_news = 0
    for source_id, titles in results.items():
        source_name = id_to_name.get(source_id, source_id)
        news_count = len(titles)
        total_news += news_count
        print(f"    {source_name}: {news_count} 条新闻")

    print(f"  - 总新闻数: {total_news}")

    # 创建测试词组配置（使用正确的结构）
    print("\n[5] 创建测试词组...")
    test_word_groups = [
        {
            "required": [],
            "normal": [{"word": "上海本地生活", "is_regex": False, "display_name": None}],
            "group_key": "上海本地生活",
            "display_name": "上海本地生活",
            "max_count": 0,
            "tags": [],
        },
        {
            "required": [],
            "normal": [{"word": "OPC", "is_regex": False, "display_name": None}],
            "group_key": "OPC",
            "display_name": "OPC",
            "max_count": 0,
            "tags": [],
        }
    ]
    print(f"✓ 测试词组创建完成")
    for group in test_word_groups:
        print(f"  - {group['display_name']}: {[w['word'] for w in group['normal']]}")

    # 执行关键词匹配
    print("\n[6] 执行关键词匹配...")
    stats, total_titles = count_word_frequency(
        results=results,
        word_groups=test_word_groups,
        filter_words=[],
        id_to_name=id_to_name,
        rank_threshold=3,
        quiet=False
    )

    print(f"✓ 关键词匹配完成")
    print(f"  - 总标题数: {total_titles}")

    # 显示采集到的样本新闻（用于诊断）
    print("\n[7] 采集到的样本新闻（前10条）:")
    print("-" * 70)
    sample_count = 0
    for source_id, titles in results.items():
        source_name = id_to_name.get(source_id, source_id)
        for title in list(titles.keys())[:3]:  # 每个源显示3条
            print(f"  [{source_name}] {title}")
            sample_count += 1
            if sample_count >= 10:
                break
        if sample_count >= 10:
            break

    # 显示匹配结果
    print("\n[8] 匹配结果详情:")
    print("-" * 70)

    for stat in stats:
        keyword_name = stat.get("keyword", "未知")
        count = stat.get("count", 0)
        print(f"\n关键词: {keyword_name}")
        print(f"  匹配数量: {count}")

        if count > 0:
            print(f"  匹配的新闻:")
            news_list = stat.get("news", [])
            for i, news in enumerate(news_list[:5], 1):  # 显示前5条
                title = news.get("title", "无标题")
                source = news.get("source", "未知来源")
                rank = news.get("rank", "N/A")
                print(f"    {i}. [{source}] (排名:{rank}) {title}")

            if len(news_list) > 5:
                print(f"    ... 还有 {len(news_list) - 5} 条新闻")
        else:
            print(f"  ⚠ 未匹配到任何新闻")

    # 总结
    print("\n" + "=" * 70)
    print("测试总结:")
    print("=" * 70)

    for stat in stats:
        keyword_name = stat.get("keyword", "未知")
        count = stat.get("count", 0)
        status = "✓ 有数据" if count > 0 else "✗ 无数据"
        print(f"{status} - {keyword_name}: {count} 条新闻")

    print("\n测试完成！")
    print("=" * 70)


if __name__ == "__main__":
    try:
        test_keywords()
    except Exception as e:
        print(f"\n❌ 测试出错: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
