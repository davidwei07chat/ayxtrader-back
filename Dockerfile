FROM python:3.10-slim

WORKDIR /app

ARG TARGETARCH
ENV SUPERCRONIC_VERSION=v0.2.39

RUN set -ex && \
    apt-get update && \
    apt-get install -y --no-install-recommends curl ca-certificates && \
    case ${TARGETARCH} in \
    amd64) \
    export SUPERCRONIC_URL=https://github.com/aptible/supercronic/releases/download/${SUPERCRONIC_VERSION}/supercronic-linux-amd64; \
    export SUPERCRONIC_SHA1SUM=c98bbf82c5f648aaac8708c182cc83046fe48423; \
    export SUPERCRONIC=supercronic-linux-amd64; \
    ;; \
    arm64) \
    export SUPERCRONIC_URL=https://github.com/aptible/supercronic/releases/download/${SUPERCRONIC_VERSION}/supercronic-linux-arm64; \
    export SUPERCRONIC_SHA1SUM=5ef4ccc3d43f12d0f6c3763758bc37cc4e5af76e; \
    export SUPERCRONIC=supercronic-linux-arm64; \
    ;; \
    *) \
    echo "Unsupported architecture: ${TARGETARCH}"; \
    exit 1; \
    ;; \
    esac && \
    for i in 1 2 3; do \
        echo "Download supercronic attempt $i/3"; \
        if curl -fsSL --connect-timeout 30 --max-time 60 -o "$SUPERCRONIC" "$SUPERCRONIC_URL"; then \
            break; \
        fi; \
        if [ $i -eq 3 ]; then \
            exit 1; \
        fi; \
        sleep 2; \
    done && \
    echo "${SUPERCRONIC_SHA1SUM}  ${SUPERCRONIC}" | sha1sum -c - && \
    chmod +x "$SUPERCRONIC" && \
    mv "$SUPERCRONIC" "/usr/local/bin/${SUPERCRONIC}" && \
    ln -s "/usr/local/bin/${SUPERCRONIC}" /usr/local/bin/supercronic && \
    supercronic -version && \
    apt-get remove -y curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY docker/requirements-main.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY docker/manage.py .
COPY docker/server.py .
COPY aiyxdata_tradar/ ./aiyxdata_tradar/
COPY config/config.example.yaml /app/default-config/config.yaml
COPY config/frequency_words.txt /app/default-config/frequency_words.txt
COPY config/timeline.yaml /app/default-config/timeline.yaml
COPY config/ai_analysis_prompt.txt /app/default-config/ai_analysis_prompt.txt
COPY config/ai_translation_prompt.txt /app/default-config/ai_translation_prompt.txt
COPY docs/index.html /app/default-output/config_editor/index.html
COPY docs/assets/ /app/default-output/config_editor/assets/
COPY docs/defaults/ /app/default-output/config_editor/defaults/

COPY docker/entrypoint.sh /entrypoint.sh.tmp
RUN sed -i 's/\r$//' /entrypoint.sh.tmp && \
    mv /entrypoint.sh.tmp /entrypoint.sh && \
    chmod +x /entrypoint.sh && \
    chmod +x manage.py && \
    mkdir -p /app/config /app/output /app/default-config /app/default-output

ENV PYTHONUNBUFFERED=1 \
    CONFIG_PATH=/app/config/config.yaml \
    FREQUENCY_WORDS_PATH=/app/config/frequency_words.txt

ENTRYPOINT ["/entrypoint.sh"]
