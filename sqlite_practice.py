#SQLite数据表练习
import sqlite3

#1创建内存数据库连接
conn = sqlite3.connect(":memory:")

#2执行SQL，创建订单表
conn.execute("""
CREATE TABLE orders(
    order_id TEXT PRIMARY KEY,
    amount INTEGER NOT NULL,
    status TEXT NOT NULL
)
""")

#3确认执行
print("orders表创建成功")

#4关闭数据库
conn.close()