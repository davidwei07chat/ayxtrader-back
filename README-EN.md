<div align="center" id="aiyxdata_tradar">

# AIYXDATA-TRADAR

**AI-powered omnichannel trend intelligence assistant**

[Quick Start](#-quick-start) | [Features](#-features) | [Config Center](#-visual-config-center) | [中文](README.md)

</div>

---

## Release Version

**Version:** `1.01.0609`

This repository is the current portable TrendRadar release. A fresh server should be able to clone this repository, run the documented Docker deployment, and get the same functional structure: hot-list/RSS configuration, visual config center, five core default config files, report generation, and the AI analysis card.

Secrets and local runtime state are intentionally not committed. Deployers must provide their own API keys, model settings, webhooks, and tokens in `.env` or in their server environment.

## Features

- Multi-platform hot-list aggregation.
- RSS/Atom feed collection.
- Keyword, alias, continuous-alias group, and category-tag configuration.
- HTML report generation and lightweight web service.
- The `✨ AI 深度分析研判` report card is always visible; if model/API key is missing, it shows configuration guidance.
- Visual config center with five fixed core files:
  - `config.yaml`
  - `frequency_words.txt`
  - `timeline.yaml`
  - `ai_analysis_prompt.txt`
  - `ai_translation_prompt.txt`
- Built-in read-only defaults live in `docs/defaults/`; deployer runtime config lives in `config/`.

## Quick Start

```bash
git clone https://github.com/davidwei07chat/ayxtrader-back.git
cd ayxtrader-back
cp .env.example .env
nano .env
docker compose up -d --build
```

Open:

```text
http://127.0.0.1:8084
http://127.0.0.1:8084/config_editor/index.html
```

On first startup, the container seeds missing runtime config files from baked defaults and syncs the config center into `output/config_editor/`.

## Visual Config Center

The config center always exposes five fixed files and a Load Defaults flow. Loading defaults reads from the read-only `docs/defaults/` templates and fills the editor. Saving writes only to the deployer's `config/` runtime files.

## Runtime State Not Published

The GitHub repository does not include real API keys, webhooks, tokens, historical reports, SQLite databases, logs, `.env`, `.env.local`, virtual environments, or local saved profiles.

## Verification

```bash
docker compose ps
docker logs -f aiyxdata_tradar
curl http://127.0.0.1:8084/config_editor/index.html
```

## License

Distributed under the [Apache License 2.0](LICENSE).
