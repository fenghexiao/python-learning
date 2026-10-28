# python-learning

Python 学习与练习代码，包含 pytest 单元测试和一个基于 FastAPI 的工具调用示例。

## 目录结构

| 文件 | 说明 |
| --- | --- |
| `greeting.py` | 基础函数示例 `greet()` |
| `tool_executor.py` | 工具执行器：`calculator` / `search` / `double` 三个工具的统一调度 |
| `api.py` | FastAPI 服务，提供 `/health` 与 `/tools/execute` 两个接口 |
| `test_basics.py` | 基础断言与参数化边界测试 |
| `test_exceptions.py` | 异常处理测试（`pytest.raises`） |
| `test_greeting.py` | `greet()` 函数测试 |
| `test_tool_executor.py` | 工具执行器测试 |
| `test_app.py` | FastAPI 接口测试（TestClient） |
| `typed_models_practice.py` | 类型标注练习：`create_order()`、`get_payment_status()`，演示标注不做运行时校验 |
| `models_practice.py` | Pydantic 练习：`Order` 模型 + 三类 `ValidationError`（类型错、越界、缺字段） |
| `practice/` | 早期练习归档（`lesson2_tool_filter.py`、`lesson7_tool_executor.py`） |

## 环境准备

```bash
pip install pytest fastapi httpx
```

## 运行测试

```bash
pytest -v
```

## 启动 API 服务

```bash
uvicorn api:app --reload
```

启动后可访问：

- `GET  /health` → `{"status": "ok"}`
- `POST /tools/execute`，请求体示例：

```json
{ "tool_name": "double", "argument": "5" }
```

返回：

```json
{ "success": true, "result": 10 }
```

## 可用工具

- `calculator` — 计算整数的平方
- `search` — 模拟搜索，返回查询字符串
- `double` — 将整数翻倍
