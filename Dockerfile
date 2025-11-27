







FROM python:3.9-slim

# 安装curl和其他必要工具
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY app/requirements.txt .
RUN pip install -r requirements.txt

# 安装测试需要的requests模块
RUN pip install requests==2.31.0

COPY app/ .

CMD ["python", "app.py"]