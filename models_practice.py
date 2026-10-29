from pydantic import BaseModel, Field, ValidationError


class Order(BaseModel):
    order_id: str = Field(min_length = 1)
    amount: int = Field(ge=0)
    assignee: str | None = None


# 下面这段演示只在直接运行本文件时执行
# 被 test_models_practice.py 导入时不会触发，避免污染测试输出
if __name__ == "__main__":
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

    # order_id 现在有 min_length=1 约束，空字符串会被拒绝
    try:
        Order(order_id="", amount=199)
    except ValidationError as e:
        print("空订单号：", e)
