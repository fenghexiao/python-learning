#创建模型
def create_order(
        order_id: str,
        amount: int,
        tags: list[str],
        assignee: str | None = None
) -> dict:
    return {
        "order_id": order_id,
        "amount": amount,
        "tags": tags,
        "assignee": assignee
    }

#实现一个判断订单是否支付的函数
def get_payment_status(paid: bool)-> str:
#如果是ture返回paid如果不是返回unpaid
    if paid:
        return "paid"
    else:
        return "unpaid"


if __name__ == "__main__":
    print(create_order("ORD-001", 199, ["urgent"], "Alice"))
    print(create_order("ORD-002", 50, []))
    print(get_payment_status(True))
    print(get_payment_status(False))

    # 关键点：类型标注不会在运行时被检查
    # 这里传的是字符串，Python 不会报错，照样执行
    print(create_order("ORD-003", "一百九十九", ["x"]))
