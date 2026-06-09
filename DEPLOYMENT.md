# AIYXDATA-TRADAR 部署指南

适用版本：`1.01.0609`

本指南对应仓库：

```text
https://github.com/davidwei07chat/ayxtrader-back.git
```

## 前置要求

- Docker 20.10+
- Docker Compose 2.0+
- Linux 服务器或本机 Docker 环境

## 标准部署

```bash
git clone https://github.com/davidwei07chat/ayxtrader-back.git
cd ayxtrader-back
cp .env.example .env
nano .env
docker compose up -d --build
```

访问：

```text
http://127.0.0.1:8084
http://127.0.0.1:8084/config_editor/index.html
```

如果需要公网访问，请让 Nginx/Caddy 反向代理到：

```text
127.0.0.1:8084
```

## 首次启动会自动生成什么

容器启动脚本会自动处理以下内容：

- 缺少 `config/config.yaml` 时，从 `config/config.example.yaml` 生成。
- 缺少 `config/frequency_words.txt`、`config/timeline.yaml`、`config/ai_analysis_prompt.txt`、`config/ai_translation_prompt.txt` 时，从镜像内置默认模板生成。
- 每次启动同步配置中心静态文件到 `output/config_editor/`，避免旧机器残留三文件配置中心。

## 必须保留的核心默认文件

以下 5 个文件必须在仓库、Docker 镜像默认模板和配置中心中同时存在：

```text
config.yaml
frequency_words.txt
timeline.yaml
ai_analysis_prompt.txt
ai_translation_prompt.txt
```

默认模板目录：

```text
docs/defaults/
```

部署者运行配置目录：

```text
config/
```

默认模板只读，用户点击“加载默认”只是把模板内容读入编辑器；保存时写入 `config/`，不会写回 `docs/defaults/`。

## AI 深度分析

报告页必须始终显示 `✨ AI 深度分析研判` 卡片：

- 未配置模型/API Key：显示前往可视化配置中心配置的提示。
- 已配置模型/API Key：正常生成 AI 研判。

配置位置：

- 可视化配置中心中的 AI 模型配置模块。
- 或 `.env` / 服务器环境变量中的 `AI_API_BASE`、`AI_API_KEY`、`AI_MODEL`。

安全要求：

- 不要把真实 API Key 写入 README、开发文档或提交到 GitHub。
- 不要提交 `.env`、`.env.local`、`.env.*.local`。
- `config/config.yaml` 在发布仓库中只保留空模板；真实值优先从 `.env` 或系统环境变量读取。

## 常用命令

```bash
docker compose ps
docker logs -f aiyxdata_tradar
docker compose restart aiyxdata_tradar
docker compose down
```

手动执行一次抓取分析：

```bash
docker exec -it aiyxdata_tradar python manage.py run
```

查看服务状态：

```bash
docker exec -it aiyxdata_tradar python manage.py status
```

## 安全边界

发布仓库不包含：

- 真实 API Key、Webhook、Token。
- 历史报告、SQLite 数据库、日志。
- `config/profiles/` 用户保存方案。
- `.env`、`.env.local`、`.env.*.local`、虚拟环境、缓存目录。

如果需要迁移旧服务器的真实配置和历史数据，请另行使用私密备份包保存 `config/`、`output/`、`data/` 和 `.env`，不要提交到公开 GitHub 仓库。

## 验证部署

```bash
curl -I http://127.0.0.1:8084/config_editor/index.html
docker logs aiyxdata_tradar | tail -50
```

页面检查：

- 配置中心显示 5 个文件。
- “加载默认”弹窗显示 5 个文件。
- 未配置 AI 时报告仍显示 `✨ AI 深度分析研判` 引导卡。
- 配置模型和 API Key 后可以生成真实 AI 研判。
