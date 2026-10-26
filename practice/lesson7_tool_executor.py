def calculate_square(value):
    try:
        number = int (value)
        return{
            "success":True,
            "result" :number *number
        }
    except ValueError:
        return{
            "success": False,
            "error": "请输入有效数字"
        }

def search(query):
        return{
            "success":True,
            "result" :"模拟搜索结果："+query
        }

tools = {
        "calculator":calculate_square,
        "search":search
    }

def execute_tool(tool_name,argument):
        if tool_name not in tools:
            return{
                "success":False,
                "error":"不存在的工具："+tool_name
            }
        tool_function = tools[tool_name]
        return tool_function(argument)

print(execute_tool("calculator", "5"))
print(execute_tool("search", "Python"))
print(execute_tool("calculator", "abc"))
print(execute_tool("unknown", "test"))