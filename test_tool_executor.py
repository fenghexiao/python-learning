from tool_executor import execute_tool
import pytest

@pytest.mark.parametrize("value, expected", [
    ("2", 4),
    ("5", 25),
    ("10", 100),
])
def test_calculator(value,expected):
    assert execute_tool("calculator", value) == {
        "success": True,
        "result": expected
    }

def test_calculator_invalid_input():
    assert execute_tool("calculator", "abc") == {
        "success": False,
        "error": "请输入有效整数"
    }


def test_search_success():
    assert execute_tool("search", "Python") == {
        "success": True,
        "result": "模拟搜索结果：Python"
    }


def test_unknown_tool():
    assert execute_tool("unknown", "test") == {
        "success": False,
        "error": "不存在的工具：unknown"
    }

def test_double_number_success():
    assert execute_tool("double", "5") == {
        "success": True,
        "result": 10
    }

def test_double_invalid_input():
    assert execute_tool("double", "abc") == {
        "success":False,
        "error": "invalid literal for int() with base 10: 'abc'"
    }
