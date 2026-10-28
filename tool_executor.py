def calculate_square(value):
    try:
        number = int(value)
        return {
            "success": True,
            "result": number * number
        }
    except ValueError:
        return {
            "success": False,
            "error":"请输入有效整数"
        }
    
def search(query):
    return {
        "success": True,
        "result": "模拟搜索结果：" + query
    }

def double_number(value): 
    try:
        number = int(value)
        return {
            "success": True,
            "result": number * 2
        }
    except ValueError as e:
        return {
            "success": False,
            "error": str(e)
        }

tools = {
    "calculator": calculate_square,
    "search": search,
    "double": double_number
}


def execute_tool(tool_name, argument):
    if tool_name not in tools:
        return {
            "success": False,
            "error": "不存在的工具：" + tool_name
        }

    tool_function = tools[tool_name]
    try:
        return tool_function(argument)
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

