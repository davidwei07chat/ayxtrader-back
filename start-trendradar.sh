#!/bin/bash
# TrendRadar 启动脚本

cd /TrendRadar
export PYTHONPATH=/TrendRadar
exec python3 -m aiyxdata_tradar
