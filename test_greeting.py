#从greeting中导入greet函数模块
from greeting import greet
def test_greet():
    assert greet ("Alice") == "Hello, Alice"
