# 新仓库迁移方案

## 目标

把当前 TrendRadar 迁移到一个新的 GitHub 仓库，同时把代码和运行数据分离。

## 推荐结构

- 新 GitHub 仓库：代码、文档、Docker、脚本、示例配置
- 私密备份包：真实配置、`output/`、`data/`、`.env`

## 新仓库应保留

- `aiyxdata_tradar/`
- `mcp_server/`
- `docker/`
- `scripts/`
- `docs/`
- `docs/defaults/`
- `config/config.example.yaml`
- `config/ai_analysis_prompt.txt`
- `config/ai_translation_prompt.txt`
- `README.md`
- `DEPLOYMENT.md`
- `docker-compose.yml`
- `Dockerfile`

## 新仓库不要提交

- `output/`
- `data/`
- `venv/`
- `.env`
- `.env.local`
- `.env.*.local`
- 真实 `config/config.yaml`
- 任何 token、webhook、password、secret

## 容易丢失的功能

### AI 深度分析研判

干净仓库里的 `config/config.yaml` 会从 `config/config.example.yaml` 生成，不包含真实 `AI_API_KEY`。真实 Key 推荐放在部署者自己的 `.env` 中，`.env` 不提交 GitHub。AI 分析区域会显示，但在没有大模型和 Key 时只显示配置提示，不会生成真实研判。

要恢复原服务器的 AI 深度分析，需要二选一：

1. 解压私密备份包里的真实 `config/config.yaml`，仅限私有服务器使用。
2. 在新服务器用 `.env` 或环境变量配置：

```bash
cp .env.example .env
nano .env
```

`.env` 示例：

```bash
AI_ANALYSIS_ENABLED=true
AI_API_KEY=你的真实APIKey
AI_MODEL=你的模型
AI_API_BASE=你的API地址
```

不要把真实 Key 提交到 GitHub。

### 可视化配置中心只显示 3 个文件

完整配置中心应包含 5 个文件：

- `config.yaml`
- `frequency_words.txt`
- `timeline.yaml`
- `ai_analysis_prompt.txt`
- `ai_translation_prompt.txt`

如果新服务器只显示 3 个文件，通常是旧的 `output/config_editor` 目录没有被刷新。当前 Docker 启动脚本会在每次启动时同步最新配置中心静态文件。

### 加载默认配置失败

配置中心的默认配置来自：

- `docs/defaults/config.yaml`
- `docs/defaults/frequency_words.txt`
- `docs/defaults/timeline.yaml`
- `docs/defaults/ai_analysis_prompt.txt`
- `docs/defaults/ai_translation_prompt.txt`
- `docs/defaults/version_configs`

这些文件必须进入新仓库，并在 Docker 镜像构建时复制到 `/app/default-output/config_editor/defaults/`。

## 迁移步骤

1. 在新目录生成干净副本。
2. 删除 `.git`、`output/`、`data/`、`venv/`。
3. 用 `config/config.example.yaml` 作为模板。
4. 新建 GitHub 仓库并 push。
5. 用私密压缩包保存真实配置和历史数据。
6. 新服务器上先 clone，再解压私密包，最后启动。

## 参考命令

```bash
cp -a /TrendRadar /TrendRadar-newrepo
cd /TrendRadar-newrepo
rm -rf .git output data venv
git init
git add .
git commit -m "init clean TrendRadar migration repo"
git branch -M main
git remote add origin https://github.com/your-name/your-new-repo.git
git push -u origin main
```

```bash
tar -czf trendradar-private-backup.tar.gz config data output .env
```

## 新服务器恢复

```bash
git clone https://github.com/your-name/your-new-repo.git
cd your-new-repo
tar -xzf /path/to/trendradar-private-backup.tar.gz
docker compose up -d --build
```

如果你不解压私密备份包，只用干净仓库启动，系统可以运行，但会使用无密钥示例配置；AI 深度分析窗口会显示配置提示，真实 AI 研判和通知渠道不会自动恢复。

## 默认配置与部署者配置隔离

- `docs/defaults/` 是内置只读模板，供配置中心“加载默认”读取。
- `config/` 是部署者运行配置，APPLY、SAVE & RUN、保存方案都写入这里。
- 用户加载默认后，只是把默认内容读入编辑器；用户修改后保存为自己的运行配置，不会写回 `docs/defaults/`。
- 5 个核心默认文件必须固定存在，不允许从默认清单中移除：
  - `config.yaml`
  - `frequency_words.txt`
  - `timeline.yaml`
  - `ai_analysis_prompt.txt`
  - `ai_translation_prompt.txt`

## 安全提醒

- 如果真实密钥曾经进入过 Git 历史，先轮换密钥。
- 新仓库建议设为 private。
- 把运行数据长期留在 Git 之外。
