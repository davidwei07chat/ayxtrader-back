#!/usr/bin/env python3
"""
Myzaker 页面分析脚本 - 补充来源标签分析
"""

import requests
import json
from pathlib import Path
from bs4 import BeautifulSoup


def analyze_myzaker_source():
    """分析 Myzaker 页面中的来源标签"""

    url = "https://www.myzaker.com/channel/10001"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Referer": "https://www.myzaker.com/",
    }

    session = requests.Session()
    session.headers.update(headers)

    print("🚀 Myzaker 来源标签分析")
    print("=" * 70)

    try:
        response = session.get(url, timeout=15)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'html.parser')

        print("📄 正在分析来源标签...")

        # 获取文章容器
        articles = soup.select('div.content-block')[:10]

        analysis = {
            "source_tag_analysis": [],
            "recommended_selectors": []
        }

        for idx, article in enumerate(articles):
            print(f"\n【文章 #{idx + 1}】")

            article_info = {
                "index": idx,
                "title": None,
                "source_tag": None,
                "source_info": None
            }

            # 获取标题
            title_el = article.find('h2', class_='article-title')
            if title_el:
                article_info["title"] = title_el.get_text(strip=True)[:50]
                print(f"标题: {article_info['title']}")

            # 尝试找来源标签 - 在文章容器内查找所有 span 和 div
            source_found = False

            # 策略 1: 查找包含特定类名的元素
            for elem in article.find_all(['span', 'div', 'a']):
                text = elem.get_text(strip=True)

                # 过滤条件：
                # 1. 文本长度在 2-30 字符之间
                # 2. 不是标题、时间、摘要
                # 3. 包含地名或媒体名称
                if 2 <= len(text) <= 30:
                    # 检查是否是地名或媒体
                    is_location = any(
                        city in text for city in
                        ['上海', '北京', '广州', '深圳', '杭州', '南京', '武汉', '成都', '西安', '天津',
                         '重庆', '苏州', '长沙', '郑州', '青岛', '宁波', '厦门', '福州', '济南', '哈尔滨',
                         '沈阳', '长春', '石家庄', '太原', '兰州', '南昌', '南宁', '贵阳', '昆明', '拉萨',
                         '乌鲁木齐', '新华社', '人民日报', '央视', '中新社', '新华网', '人民网', '央广网',
                         '中国新闻网', '光明网', '中国日报', '国际在线', '中国网', '中国青年网', '中国经济网']
                    )

                    if is_location and not source_found:
                        article_info["source_tag"] = text
                        article_info["source_info"] = {
                            "text": text,
                            "tag": elem.name,
                            "class": elem.get('class', []),
                            "id": elem.get('id', '')
                        }
                        print(f"✅ 找到来源标签: '{text}'")
                        print(f"   - 标签: {elem.name}")
                        print(f"   - 类名: {elem.get('class', [])}")
                        source_found = True
                        break

            if not source_found:
                print(f"⚠️  未找到来源标签")

            analysis["source_tag_analysis"].append(article_info)

        # 统计来源标签
        sources_found = [a for a in analysis["source_tag_analysis"] if a["source_tag"]]
        print(f"\n" + "=" * 70)
        print(f"📊 来源标签提取统计")
        print(f"=" * 70)
        print(f"成功提取: {len(sources_found)}/{len(analysis['source_tag_analysis'])}")

        if sources_found:
            print(f"\n✅ 提取的来源标签示例:")
            for article in sources_found[:5]:
                print(f"   - {article['source_tag']}")

            # 分析选择器
            print(f"\n🔍 来源标签选择器分析:")
            print(f"   - 标签类型: span, div, a")
            print(f"   - 文本长度: 2-30 字符")
            print(f"   - 包含内容: 地名或媒体名称")
            print(f"   - 推荐选择器: span, div, a (需要按文本内容过滤)")

        # 保存分析结果
        output_file = Path("/tmp/myzaker_source_analysis.json")
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(analysis, f, ensure_ascii=False, indent=2)

        print(f"\n✅ 详细分析已保存到: {output_file}")

    except Exception as e:
        print(f"❌ 分析失败: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    analyze_myzaker_source()
