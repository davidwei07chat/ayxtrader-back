#!/usr/bin/env python3
"""
Myzaker 页面分析脚本 - 精确版
识别真正的文章卡片容器和选择器
"""

import requests
import json
from pathlib import Path
from bs4 import BeautifulSoup
import time


def analyze_myzaker_detailed():
    """详细分析 Myzaker 页面结构"""

    channels = [
        {"id": "10001", "name": "热点", "url": "https://www.myzaker.com/channel/10001"},
        {"id": "660", "name": "24小时综合", "url": "https://www.myzaker.com/channel/660"},
    ]

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Referer": "https://www.myzaker.com/",
    }

    session = requests.Session()
    session.headers.update(headers)

    for channel in channels:
        print(f"\n{'='*70}")
        print(f"详细分析频道: {channel['name']} ({channel['id']})")
        print(f"URL: {channel['url']}")
        print(f"{'='*70}")

        try:
            # 获取页面
            print("📄 正在加载页面...")
            response = session.get(channel['url'], timeout=15)
            response.encoding = 'utf-8'

            if response.status_code != 200:
                print(f"❌ HTTP 错误: {response.status_code}")
                continue

            print(f"✅ 页面加载成功 ({len(response.text)} 字节)")

            # 解析 HTML
            soup = BeautifulSoup(response.text, 'html.parser')

            # 获取页面标题
            page_title = soup.title.string if soup.title else "N/A"
            print(f"📊 页面标题: {page_title}")

            # 分析结果
            analysis = {
                "page_title": page_title,
                "url": channel['url'],
                "channel_id": channel['id'],
                "channel_name": channel['name'],
                "recommended_selectors": [],
                "articles": [],
                "page_structure": {}
            }

            # 更精确的选择器 - 针对文章卡片
            article_selectors = [
                # 主要文章卡片
                ('div.news-item', 'div.news-item'),
                ('div[class*="news-item"]', 'div.news-item*'),
                ('div[class*="article-item"]', 'div.article-item*'),
                ('div[class*="feed-item"]', 'div.feed-item*'),

                # 内容块
                ('div.content-wrap', 'div.content-wrap'),
                ('div.content-block', 'div.content-block'),
                ('div.article-content', 'div.article-content'),

                # 通用容器
                ('div[class*="card"]', 'div.card*'),
                ('li[class*="item"]', 'li.item*'),
                ('article', 'article'),
            ]

            print(f"\n🔎 精确选择器分析...")

            for selector, display_name in article_selectors:
                try:
                    elements = soup.select(selector)
                    count = len(elements)

                    if count > 0:
                        # 检查这些元素是否包含文章特征
                        has_title = False
                        has_link = False
                        has_time = False

                        for elem in elements[:3]:
                            text = elem.get_text(strip=True)
                            if len(text) > 20:
                                has_title = True
                            if elem.find('a', href=True):
                                has_link = True
                            if any(kw in text for kw in ['分钟', '小时', '天', '前']):
                                has_time = True

                        is_article_container = has_title and has_link

                        analysis["recommended_selectors"].append({
                            "selector": selector,
                            "display_name": display_name,
                            "count": count,
                            "has_title": has_title,
                            "has_link": has_link,
                            "has_time": has_time,
                            "is_article_container": is_article_container,
                            "viable": 3 <= count <= 100
                        })

                        status = "✓" if is_article_container else "○"
                        print(f"   {status} {display_name}: {count} 个 (标题:{has_title} 链接:{has_link} 时间:{has_time})")

                except Exception as e:
                    pass

            # 找到最佳选择器
            best_selector = None
            for sel_info in analysis["recommended_selectors"]:
                if sel_info["is_article_container"] and sel_info["viable"]:
                    best_selector = sel_info["selector"]
                    break

            if best_selector:
                print(f"\n✅ 推荐选择器: {best_selector}")

                # 详细分析文章
                articles = soup.select(best_selector)[:10]
                print(f"\n📝 详细分析前 {len(articles)} 个文章:\n")

                for idx, article in enumerate(articles):
                    item = {
                        "rank": idx + 1,
                        "tag": article.name,
                        "classes": article.get('class', []),
                        "id": article.get('id', ''),
                        "html_structure": {
                            "title": None,
                            "link": None,
                            "time": None,
                            "summary": None,
                            "image": None,
                            "source": None
                        }
                    }

                    # 提取标题
                    for tag in ['h1', 'h2', 'h3', 'h4', 'a']:
                        title_el = article.find(tag)
                        if title_el and len(title_el.get_text(strip=True)) > 5:
                            item["html_structure"]["title"] = {
                                "tag": tag,
                                "class": title_el.get('class', []),
                                "text": title_el.get_text(strip=True)
                            }
                            break

                    # 提取链接
                    link_el = article.find('a', href=True)
                    if link_el:
                        href = link_el['href']
                        # 补全相对 URL
                        if href.startswith('//'):
                            href = 'https:' + href
                        elif href.startswith('/'):
                            href = 'https://www.myzaker.com' + href

                        item["html_structure"]["link"] = {
                            "tag": "a",
                            "href": href,
                            "class": link_el.get('class', [])
                        }

                    # 提取时间
                    time_el = article.find(['time', 'span', 'div'], class_=lambda x: x and 'time' in str(x).lower())
                    if not time_el:
                        # 尝试查找包含时间关键词的元素
                        for elem in article.find_all(['span', 'div']):
                            text = elem.get_text(strip=True)
                            if any(kw in text for kw in ['分钟', '小时', '天', '昨天', '前']) and len(text) < 20:
                                time_el = elem
                                break

                    if time_el:
                        item["html_structure"]["time"] = {
                            "tag": time_el.name,
                            "class": time_el.get('class', []),
                            "text": time_el.get_text(strip=True)
                        }

                    # 提取摘要
                    summary_el = article.find('p')
                    if not summary_el:
                        summary_el = article.find('div', class_=lambda x: x and any(kw in str(x).lower() for kw in ['summary', 'desc', 'content']))

                    if summary_el and len(summary_el.get_text(strip=True)) > 20:
                        item["html_structure"]["summary"] = {
                            "tag": summary_el.name,
                            "class": summary_el.get('class', []),
                            "text": summary_el.get_text(strip=True)[:100]
                        }

                    # 提取图片
                    img_el = article.find('img')
                    if img_el:
                        src = img_el.get('src', '')
                        if src.startswith('//'):
                            src = 'https:' + src
                        item["html_structure"]["image"] = {
                            "src": src,
                            "alt": img_el.get('alt', ''),
                            "class": img_el.get('class', [])
                        }

                    # 提取来源
                    source_el = article.find(['span', 'div'], class_=lambda x: x and 'source' in str(x).lower())
                    if source_el:
                        item["html_structure"]["source"] = {
                            "tag": source_el.name,
                            "text": source_el.get_text(strip=True)
                        }

                    analysis["articles"].append(item)

                    # 打印文章信息
                    print(f"   【文章 #{idx + 1}】")
                    if item["html_structure"]["title"]:
                        print(f"   标题: {item['html_structure']['title']['text']}")
                    if item["html_structure"]["link"]:
                        print(f"   链接: {item['html_structure']['link']['href']}")
                    if item["html_structure"]["time"]:
                        print(f"   时间: {item['html_structure']['time']['text']}")
                    if item["html_structure"]["summary"]:
                        print(f"   摘要: {item['html_structure']['summary']['text']}")
                    if item["html_structure"]["image"]:
                        print(f"   图片: {item['html_structure']['image']['src'][:60]}...")
                    print()

            else:
                print("⚠️  未找到合适的文章选择器")

            # 保存详细分析结果
            output_file = Path(f"/tmp/myzaker_analysis_detailed_{channel['id']}.json")
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(analysis, f, ensure_ascii=False, indent=2)
            print(f"✅ 详细分析已保存到: {output_file}")

            # 短暂延迟
            time.sleep(2)

        except Exception as e:
            print(f"❌ 分析失败: {e}")
            import traceback
            traceback.print_exc()


if __name__ == "__main__":
    print("🚀 Myzaker 页面详细分析工具")
    print("=" * 70)

    try:
        analyze_myzaker_detailed()
        print("\n" + "=" * 70)
        print("✅ 分析完成！")
        print("=" * 70)

    except KeyboardInterrupt:
        print("\n⏹️  用户中断")
    except Exception as e:
        print(f"\n❌ 错误: {e}")
        import traceback
        traceback.print_exc()
