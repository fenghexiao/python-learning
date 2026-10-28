from pydantic import BaseModel, Field, ValidationError


class Order(BaseModel):
    order_id: str
    amount: int = Field(ge=0)
    assignee: str | None = None


# 合法数据：直接构造成功
order1 = Order(order_id="ORD-001", amount=199)
print(order1)

order2 = Order(order_id="ORD-002", amount=0, assignee="Alice")
print(order2)

# 创建一个捕获验证异常
# 非法字段：金额为负，被 Field(ge=0) 拦下
try:
    Order(order_id="ORD-003", amount=-1)
except ValidationError as e:
    print("金额非法：", e)

# 非法类型：assignee 应该是字符串，传了整数
try:
    Order(order_id="ORD-004", amount=199, assignee=123)
except ValidationError as e:
    print("类型非法：", e)

# 还差一点：缺必填字段 order_id
try:
    Order(amount=199)
except ValidationError as e:
    print("缺字段：", e)
