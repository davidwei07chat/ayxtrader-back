<div align="center" id="aiyxdata_tradar">

# AIYXDATA-TRADAR

**AI 驱动的全渠道热点情报助手**

[快速部署](#-快速部署) | [核心功能](#-核心功能) | [配置中心](#-可视化配置中心) | [English](README-EN.md)

</div>

---

## 当前发布版本

**版本:** `1.01.0609`

本仓库是 TrendRadar 当前可迁移发布版，目标是让新服务器按本文档部署后，保留当前功能结构、RSS/热榜配置、可视化配置中心、5 个核心配置文件默认模板，以及 AI 深度分析展示入口。

为了安全，仓库不会提交真实 API Key、Webhook、历史报告、SQLite 数据库或本机缓存。新部署者需要在可视化配置中心或环境变量中填写自己的模型和通知配置。

## 核心功能

- 多平台热榜抓取与聚合。
- RSS/Atom 订阅源抓取。
- 关键词、别名、连续别名组和分类标签配置。
- HTML 报告生成与轻量 Web 服务。
- `✨ AI 深度分析研判` 报告卡片始终显示；未配置模型/API Key 时显示配置引导。
- 可视化配置中心支持 5 个固定核心文件：
  - `config.yaml`
  - `frequency_words.txt`
  - `timeline.yaml`
  - `ai_analysis_prompt.txt`
  - `ai_translation_prompt.txt`
- 内置只读默认模板位于 `docs/defaults/`，部署者运行配置位于 `config/`，二者互不覆盖。

## 快速部署

### 1. 克隆仓库

```bash
git clone https://github.com/davidwei07chat/ayxtrader-back.git
cd ayxtrader-back
```

### 2. 启动 Docker 服务

```bash
docker compose up -d --build
```

启动后访问：

```text
http://127.0.0.1:8084
http://127.0.0.1:8084/config_editor/index.html
```

容器首次启动时会自动完成：

- 如果 `config/config.yaml` 不存在，从 `config/config.example.yaml` 生成。
- 如果 5 个核心配置文件缺失，从镜像内置默认模板生成。
- 同步可视化配置中心静态文件到 `output/config_editor/`。

### 3. 配置 AI 和通知

推荐用 `.env` 保存所有密钥，不要把真实 Key 写进 Git 仓库：

```bash
cp .env.example .env
nano .env
docker compose up -d --build
```

`.env` 已在 `.gitignore` 中排除，不会进入发布仓库。打开右下角可视化配置中心，或直接编辑 `.env`：

- `AI_API_BASE`
- `AI_API_KEY`
- `AI_MODEL`
- 各通知渠道 Webhook/Token

未配置 AI 时，系统仍会正常生成报告，并显示 `✨ AI 深度分析研判` 配置提示卡；配置完成后即可生成真实 AI 研判内容。

## 可视化配置中心

配置中心入口：

```text
http://127.0.0.1:8084/config_editor/index.html
```

配置中心固定显示 5 个文件，不能删除、移动或改名。点击“加载默认”只会从 `docs/defaults/` 读取内置模板并填充到编辑器；用户保存时写入自己的 `config/` 运行配置，不会修改默认模板。

## 目录说明

```text
config/                 # 部署者运行配置，首次部署可由默认模板生成
docs/defaults/          # 5 个核心文件的内置只读默认模板
docs/index.html         # 配置中心静态模板
docs/assets/            # 配置中心前端资源
docker/                 # Docker 构建、启动和 Web API
aiyxdata_tradar/        # 主程序源码
output/                 # 运行时生成目录，不随仓库发布
```

## 不随仓库发布的本地状态

以下内容不会进入 GitHub 发布仓库：

- 真实 API Key、Webhook、Token。
- `.env`、`.env.local`、`.env.*.local`。
- `output/` 历史报告、数据库和日志。
- `data/` 本地数据。
- `config/profiles/` 用户保存方案。
- 虚拟环境、缓存目录。

## 验证命令

```bash
docker compose ps
docker logs -f aiyxdata_tradar
curl http://127.0.0.1:8084/config_editor/index.html
```

## 迁移说明

详细迁移方案见：

- `docs/NEW_REPO_MIGRATION.md`
- `docs/202603071010 Visual_Config_Integration_Manual.md`
- `docs/202605121330 Homepage_Development_Documentation.md`
- `docs/202604251430 Homepage_Technical_Documentation.md`

## 许可证

本项目采用 [Apache License 2.0](LICENSE) 开源协议。
