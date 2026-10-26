#TestClient 在测试中模拟http请求
from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

def test_health():
    response = client.get ("/health")

    assert response.status_code==200
    assert response.json() == {"status" : "ok"}

def test_execute_tool():
    response = client.post("/tools/execute", json={"tool_name": "double", "argument": "5"})

    assert response.status_code == 200
    assert response.json() == {"success": True, "result": 10}