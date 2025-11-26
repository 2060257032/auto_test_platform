#!/bin/bash
echo "开始测试..."

# 启动服务
docker-compose up -d
sleep 15  # 增加等待时间

# 运行测试
cd tests
pip install -r requirements.txt
python -m pytest test_app.py -v

echo "测试完成"