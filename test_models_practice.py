#用 pytest.raises 检查异常是否真的发生。
import pytest
from pydantic import ValidationError
from models_practice import Order
  
#创建订单
def test_order_model():
    order = Order(order_id="ORD-001", amount=199, assignee=None)
    #检查
    assert order.amount == 199
    assert order.assignee == None   

def test_order_negative_amount():    
    with pytest.raises(ValidationError):
        Order(order_id="ORD-002", amount=-1)

#创建订单是不填金额
def test_order_missing_amount():
    with pytest.raises(ValidationError):
        Order(order_id="ORD-003")        

#创建订单时乱填assignee类型
def test_order_invalid_assignee():
    with pytest.raises(ValidationError):
        Order(order_id="ORD-004", amount=199, assignee=123)

#多个数据的pytest.mark.parametrize测试
@pytest.mark.parametrize("amount",[0,1,199])
def test_order_valid_amounts(amount):
    order1 = Order(order_id="ORD-005", amount=amount)
    assert order1.amount == amount
#空字符id测试
def test_order_rejects_empty_order_id():
    with pytest.raises(ValidationError):
        Order(order_id="", amount=199)

#pytest。fixture 测试夹具
@pytest.fixture
def sample_order():
    return Order(order_id="ORD-006", amount=199, assignee="Alice")

def test_order_fixture(sample_order):
    assert sample_order.order_id == "ORD-006"
    assert sample_order.amount == 199
    assert sample_order.assignee == "Alice"