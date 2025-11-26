import requests
import time

def test_app_running():
    """测试应用是否运行"""
    time.sleep(5)  # 等待应用启动
    response = requests.get('http://localhost:5000/')
    assert response.status_code == 200
    assert 'Hello' in response.text

def test_visitor_count():
    """测试访问计数"""
    response = requests.get('http://localhost:5000/api/visitors')
    assert response.status_code == 200
    data = response.json()
    assert 'visitor_count' in data