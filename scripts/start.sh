#!/bin/bash
echo "启动应用..."
docker-compose up -d
echo "应用已启动！"
echo "等待服务启动..."
sleep 10
echo "请访问: https://$CODESPACE_NAME-5000.preview.app.github.dev"