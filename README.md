# auto_test_platform
简单云docker测试平台
# 简单云Docker测试平台

## 快速开始
1. 点击右侧 "Open in Gitpod" 按钮启动环境
2. 在终端执行: `./scripts/start.sh`
3. 等待启动完成，访问自动打开的浏览器窗口
4. 运行测试: `./scripts/test.sh`

## 功能特性
- ✅ Web应用 (Flask)
- ✅ Redis数据存储  
- ✅ 自动化测试
- ✅ CI/CD流水线

## 项目结构
├── app/ # Web应用
│ ├── app.py
│ └── requirements.txt
├── tests/ # 测试用例
│ ├── test_app.py
│ └── requirements.txt
├── scripts/ # 自动化脚本
│ ├── start.sh
│ └── test.sh
├── Dockerfile
├── docker-compose.yml
└── README.md