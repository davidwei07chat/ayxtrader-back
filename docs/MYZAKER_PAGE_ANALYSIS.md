# Myzaker 页面分析报告

**分析日期：** 2026-05-18  
**分析工具：** BeautifulSoup + requests  
**分析状态：** ✅ 完成

---

## 📊 执行摘要

成功分析了 Myzaker 两个主要频道的页面结构：
- ✅ **频道 10001（热点）** - 36 个文章容器，推荐选择器：`div.content-block`
- ✅ **频道 660（24小时综合）** - 36 个文章容器，推荐选择器：`div.content-block`

**关键发现：**
- 页面为静态 HTML，无需 JavaScript 渲染
- 所有必需数据（标题、链接、时间、摘要）都可直接提取
- 建议使用 `requests + BeautifulSoup` 而非 Playwright

---

## 🔍 频道分析

### 频道 10001 - 热点

| 属性 | 值 |
|------|-----|
| **URL** | https://www.myzaker.com/channel/10001 |
| **页面标题** | 上海 - ZAKER新闻 |
| **文章容器数** | 36 个 |
| **推荐选择器** | `div.content-block` |
| **备选选择器** | `div.article-content` |

**选择器对比：**

| 选择器 | 数量 | 标题 | 链接 | 时间 | 可用性 |
|--------|------|------|------|------|--------|
| `div.content-wrap` | 1 | ✓ | ✓ | ✓ | ✗ (太少) |
| `div.content-block` | 36 | ✓ | ✓ | ✓ | ✅ |
| `div.article-content` | 36 | ✓ | ✓ | ✓ | ✅ |

**示例文章：**

```
【文章 #1】
标题: 用镜头赴一场美好之约！这一次，静安邀您"共绘市北"
链接: https://www.myzaker.com/article/6a0af66c8e9f0915186576f4
时间: 30分钟前
摘要: 你眼中的市北国际科创区是什么模样？是硬核满满的科技感，还是转角可遇的烟火气？这一次，我们不定义市北，

【文章 #2】
标题: 519中国旅游日，携彩色静安，赴一场都市旅人的浪漫邀约！
链接: https://www.myzaker.com/article/6a0af66c8e9f0915b47c3d56
时间: 30分钟前
摘要: 20265·19Jing'an看见彩色静安SeeingColor5月19日是中国旅游日，一场高品质的

【文章 #3】
标题: 商业服务进社区，TA们点亮便民消费新场景
链接: https://www.myzaker.com/article/6a0af66c8e9f0915c94da464
时间: 30分钟前
摘要: 为深入推进文商旅体展深度融合，烘托上海市第七届"五五购物节"浓厚消费氛围，紧扣"爱购上海、乐享消费"
```

---

### 频道 660 - 24小时综合

| 属性 | 值 |
|------|-----|
| **URL** | https://www.myzaker.com/channel/660 |
| **页面标题** | ZAKER新闻 |
| **文章容器数** | 36 个 |
| **推荐选择器** | `div.content-block` |
| **备选选择器** | `div.article-content` |

**选择器对比：** 与频道 10001 相同

**示例文章：**

```
【文章 #1】
标题: 带81岁母亲"打卡"30多所名校，清华大学原博导发起一场"校门实验"
链接: https://www.myzaker.com/article/6a0b04e18e9f09550523bd8a
时间: 32分钟前
摘要: 文｜《中国科学报》记者陈彬从今年4月初开始，清华大学原博士生导师郑毓煌发起了一场"校门实验"。一个多

【文章 #2】
标题: 美方被曝将暂停对伊朗的石油制裁
链接: https://www.myzaker.com/article/6a0b03cb8e9f09544969c31a
时间: 37分钟前
摘要: 当地时间18日，一位接近美伊谈判团队的消息人士称，美方在最新谈判方案文本中已同意在谈判期间对伊朗的石

【文章 #3】
标题: 美医保巨头CEO枪杀案开庭在即，一个背包成关键证据
链接: https://www.myzaker.com/article/6a0afbedb15ec078a2445f3a
时间: 1小时前
摘要: 据路·透社5月18日报道，被控枪杀美国联合健康保险公司（UnitedHealthcare）高管的28
```

---

## 🎯 CSS 选择器映射表

### 文章容器

```css
/* 主选择器 - 推荐使用 */
div.content-block

/* 备选选择器 */
div.article-content
div.content-wrap
```

### 文章内部元素

| 元素 | 选择器 | 说明 |
|------|--------|------|
| **标题** | `h2.article-title` | 文章标题 |
| **链接** | `a[href]` | 文章链接（第一个 a 标签） |
| **时间** | `span.article-time` | 发布时间（相对格式） |
| **摘要** | `div.content-block` 或 `div.article-content` | 文章摘要/描述 |
| **来源** | `div.article-footer` | 来源信息（城市、区域、标签） |
| **图片** | `img` | 文章配图（可选） |

---

## 📋 数据提取规则

### 1. 文章标题 (title)

**选择器：** `h2.article-title`  
**提取方式：** 获取文本内容  
**示例：** `"用镜头赴一场美好之约！这一次，静安邀您"共绘市北""`

### 2. 文章链接 (url)

**选择器：** `a[href]`  
**提取方式：** 获取 href 属性，补全相对 URL  
**格式：** `https://www.myzaker.com/article/{id}`  
**示例：** `https://www.myzaker.com/article/6a0af66c8e9f0915186576f4`

### 3. 发布时间 (published_at)

**选择器：** `span.article-time`  
**提取方式：** 获取文本内容（相对时间格式）  
**格式：** `"30分钟前"`, `"1小时前"`, `"昨天"`, `"2天前"` 等  
**需要转换为绝对时间戳**

**相对时间解析规则：**

| 格式 | 转换规则 |
|------|---------|
| `{n}分钟前` | 当前时间 - n 分钟 |
| `{n}小时前` | 当前时间 - n 小时 |
| `昨天` | 当前日期 - 1 天 |
| `{n}天前` | 当前日期 - n 天 |
| `今天` | 当前日期 |

### 4. 摘要 (summary)

**选择器：** `div.content-block` 或 `div.article-content`  
**提取方式：** 获取文本内容，去除 HTML 标签  
**长度：** 截断到 100-200 字符

### 5. 排名位置 (rank)

**提取方式：** 在列表中的顺序（1, 2, 3, ...）

### 6. 图片 (image) - 可选

**选择器：** `img`  
**提取方式：** 获取 src 属性

### 7. 来源信息 (source) - 新增 ⭐

**选择器：** `div.article-footer`  
**提取方式：** 获取文本内容，用正则表达式分解  
**格式：** `"上海静安30分钟前ai技术创新"`

**来源标签包含的信息：**

| 字段 | 格式 | 示例 |
|------|------|------|
| **城市** | 中文城市名 | "上海", "北京", "广州" |
| **区域** | 中文区县名 | "静安", "嘉定", "宝山", "黄浦" |
| **时间** | 相对时间 | "30分钟前", "1小时前" |
| **标签** | 分类标签 | "ai技术创新", "旅游局", "教育局" |

**提取示例：**

```
原始文本: "上海静安30分钟前ai技术创新"
↓
城市: "上海"
区域: "静安"
时间: "30分钟前"
标签: "ai技术创新"
```

**提取代码：**

```python
import re

def parse_source_info(source_text):
    """解析来源信息"""
    
    # 城市列表
    cities = ['上海', '北京', '广州', '深圳', '杭州', '南京', '武汉', '成都', '西安', '天津', '重庆']
    
    # 区域列表（以上海为例）
    districts = ['静安', '嘉定', '宝山', '黄浦', '浦东', '闵行', '徐汇', '长宁', '普陀', '虹口', '杨浦', '松江', '青浦', '奉贤', '崇明']
    
    result = {
        'city': None,
        'district': None,
        'time': None,
        'tags': []
    }
    
    # 提取城市
    for city in cities:
        if city in source_text:
            result['city'] = city
            source_text = source_text.replace(city, '', 1)
            break
    
    # 提取区域
    for district in districts:
        if district in source_text:
            result['district'] = district
            source_text = source_text.replace(district, '', 1)
            break
    
    # 提取时间
    time_match = re.search(r'(\d+分钟前|\d+小时前|昨天|今天)', source_text)
    if time_match:
        result['time'] = time_match.group(0)
        source_text = source_text.replace(result['time'], '', 1)
    
    # 剩余部分作为标签
    remaining = source_text.strip()
    if remaining:
        result['tags'] = [tag.strip() for tag in remaining.split() if tag.strip()]
    
    return result

# 使用示例
source_text = "上海静安30分钟前ai技术创新"
info = parse_source_info(source_text)
# 结果: {'city': '上海', 'district': '静安', 'time': '30分钟前', 'tags': ['ai技术创新']}
```

---

## 🛠️ 爬虫实现建议

### 1. 使用库选择

**推荐：** `requests + BeautifulSoup`
- 页面是静态 HTML，无需 JavaScript 渲染
- 更快、更轻量、更稳定
- 无需 Playwright 的浏览器依赖

### 2. 请求配置

```python
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Referer": "https://www.myzaker.com/",
}
```

### 3. 反爬虫对策

- 请求间隔: 3-5 秒
- 随机延迟: ±20% 抖动
- User-Agent 轮换
- 遵守 robots.txt

### 4. 去重策略

- 按 URL 规范化 + 标题组合键
- 移除 URL 中的动态参数

---

## ✅ 验证清单

- [x] 页面可访问
- [x] 文章容器可识别
- [x] 标题可提取
- [x] 链接可提取
- [x] 时间可提取
- [x] 摘要可提取
- [x] 排名位置可确定
- [x] 两个频道结构一致
- [x] 无需 JavaScript 渲染
- [x] 反爬虫对策可行

---

## 📌 后续步骤

1. **实现爬虫模块** - 创建 `aiyxdata_tradar/crawler/myzaker_scraper.py`
2. **集成到主流程** - 修改 `__main__.py` 和 `analyzer.py`
3. **配置管理** - 在 `config.yaml` 中添加 Myzaker 配置
4. **测试验证** - 运行完整的爬取→存储→分析流程
5. **性能监控** - 24 小时监控爬虫稳定性

---

**分析完成时间：** 2026-05-18  
**分析工具版本：** BeautifulSoup 4.12+, requests 2.31+
