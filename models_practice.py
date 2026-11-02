
from pydantic import BaseModel, Field, ValidationError, model_validator


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

    @model_validator(mode="after")
    def validate_arguments_match_tool_(self):
        if self.tool_name == "get_order":
            if not isinstance(self.arguments, GetOrderArgs):
                raise ValueError("get_order 必须使用 GetOrderArgs")

        elif self.tool_name == "create_ticket":
            if not isinstance(self.arguments, CreateTicketArgs):
                raise ValueError("create_ticket 必须使用 CreateTicketArgs")
        else:
            raise ValueError(f"不支持的工具: {self.tool_name}")

        return self

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
    try:
        mismatch_call = ToolCall(
            tool_name="get_order",
            arguments={
                "title": "订单异常",
                "description": "订单状态未更新"
            }
        )
    except ValidationError as e:
        print("不匹配的调用：", e.errors())

    # 测试：工具名称与参数类型不匹配
    try:
        ToolCall(
            tool_name="get_order",
            arguments=CreateTicketArgs
            (title="订单异常",description="订单状态未更新")
        )
    except ValidationError as e:
        print("不匹配的调用被拦截：", e.errors())

    #测试：不支持的工具名称
    try:
        ToolCall(
            tool_name="delete_order",
            arguments=GetOrderArgs
            (order_id="ORD-007")
        )
    except ValidationError as e:
        print("未知工具被拦截：", e.errors())
