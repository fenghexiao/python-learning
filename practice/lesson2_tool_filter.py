tools = [
    {"name" : "calculater","enabled" : True},
    {"name" : "serch", "enabled" : False}
]

tools.append({"name" : "datebase" , "enabled" : True})

for tool in tools:
    print(tool["name"], tool["enabled"])
    if tool["enabled"] == True:
        print(tool["name"])