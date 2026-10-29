
from pydantic import BaseModel, Field, ValidationError


# 练习一：订单模型
class Order(BaseModel):
    order_id: str = Field(min_length=1)
    amount: int = Field(ge=0)
    assignee: str | None = None


# 练习二：查询订单所需的参数
class GetOrderArgs(BaseModel):
    order_id: str = Field(min_length=1)

#创建模拟订单模型
class CreateTicketArgs(BaseModel):
    title : str = Field(min_length=1)
    description : str=Field(min_length=1)


# 练习三：工具调用模型
class ToolCall(BaseModel):
    tool_name: str = Field(min_length=1)
    arguments: GetOrderArgs | CreateTicketArgs


if __name__ == "__main__":
    # 1. Order：合法输入
    order = Order(order_id="ORD-001", amount=199)
    print("合法订单：", order)

    # 2. Order：非法金额
    try:
        Order(order_id="ORD-002", amount=-1)
    except ValidationError as e:
        print("金额校验失败：", e.errors())

    # 3. GetOrderArgs：合法参数
    args = GetOrderArgs(order_id="ORD-003")
    print("合法工具参数：", args)

    # 4. ToolCall：字典参数会被解析为 GetOrderArgs
    call = ToolCall(
        tool_name="get_order",
        arguments=GetOrderArgs(order_id="ORD-004")
    )
    print("合法工具调用：", call)
    print("工具名称：", call.tool_name)
    print("订单编号：", call.arguments.order_id)

    # 5. ToolCall：空订单编号应该被拦截
    try:
        ToolCall(
            tool_name="get_order",
            arguments=GetOrderArgs(order_id="")
        )
    except ValidationError as e:
        print("工具参数校验失败：", e.errors())

    # 6. ToolCall：空工具名称也应该被拦截
    try:
        ToolCall(
            tool_name="",
            arguments=GetOrderArgs(order_id="ORD-005")
        )
    except ValidationError as e:
        print("工具名称校验失败：", e.errors())


    #测试一 ： 查询订单
    order_call = ToolCall(
        tool_name="get_order",
        arguments=GetOrderArgs(order_id="ORD-006")
    )
    print("查询订单工具：", order_call)
    print("参数模型：", type(order_call.arguments).__name__)

    #测试二 ： 创建工单
    ticket_call = ToolCall(
        tool_name="create_ticket",
        arguments=CreateTicketArgs(title="订单异常", description="订单状态未更新")
    )
    print("创建工单：", ticket_call)
    print("参数模型：", type(ticket_call.arguments).__name__)

    #测试三 ： 创建工单时，标题不能空
    try:
        ToolCall(
            tool_name="create_ticket",
            arguments=CreateTicketArgs(title="",description="订单状态未更新")
        )
    except ValidationError as e:
        print("工单参数校验失败:",e.errors())


        # 测试：工具名称与参数类型不匹配
    mismatch_call = ToolCall(
        tool_name="get_order",
        arguments={
            "title": "订单异常",
            "description": "订单状态未更新"
        }
    )
    print("不匹配的调用：", mismatch_call)
