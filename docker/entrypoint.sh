#!/bin/bash
set -e

mkdir -p /app/config /app/output

seed_file() {
    local src="$1"
    local dest="$2"
    if [ ! -f "$dest" ] && [ -f "$src" ]; then
        mkdir -p "$(dirname "$dest")"
        cp "$src" "$dest"
        echo "✅ 已生成默认配置: $dest"
    fi
}

seed_file "/app/default-config/config.yaml" "/app/config/config.yaml"
seed_file "/app/default-config/frequency_words.txt" "/app/config/frequency_words.txt"
seed_file "/app/default-config/timeline.yaml" "/app/config/timeline.yaml"
seed_file "/app/default-config/ai_analysis_prompt.txt" "/app/config/ai_analysis_prompt.txt"
seed_file "/app/default-config/ai_translation_prompt.txt" "/app/config/ai_translation_prompt.txt"

if [ -d "/app/default-output/config_editor" ]; then
    mkdir -p /app/output/config_editor
    cp -a /app/default-output/config_editor/. /app/output/config_editor/
    echo "✅ 已同步配置中心静态文件: /app/output/config_editor"
fi

if [ ! -f "/app/config/config.yaml" ] || [ ! -f "/app/config/frequency_words.txt" ]; then
    echo "❌ 配置文件缺失"
    exit 1
fi

# 保存环境变量
env >> /etc/environment

case "${RUN_MODE:-cron}" in
"once")
    echo "🔄 单次执行"
    exec /usr/local/bin/python -m aiyxdata_tradar
    ;;
"cron")
    # 生成 crontab
    echo "${CRON_SCHEDULE:-*/30 * * * *} cd /app && /usr/local/bin/python -m aiyxdata_tradar" > /tmp/crontab
    
    echo "📅 生成的crontab内容:"
    cat /tmp/crontab

    if ! /usr/local/bin/supercronic -test /tmp/crontab; then
        echo "❌ crontab格式验证失败"
        exit 1
    fi

    # 启动 Web 服务器（如果配置了）
    if [ "${ENABLE_WEBSERVER:-false}" = "true" ]; then
        echo "🌐 启动 Web 服务器..."
        cd /app && /usr/local/bin/python manage.py start_webserver
    fi

    # 立即执行一次（如果配置了）
    if [ "${IMMEDIATE_RUN:-false}" = "true" ]; then
        echo "▶️ 立即执行一次"
        /usr/local/bin/python -m aiyxdata_tradar
    fi

    echo "⏰ 启动supercronic: ${CRON_SCHEDULE:-*/30 * * * *}"
    echo "🎯 supercronic 将作为 PID 1 运行"

    exec /usr/local/bin/supercronic -passthrough-logs /tmp/crontab
    ;;
*)
    exec "$@"
    ;;
esac
