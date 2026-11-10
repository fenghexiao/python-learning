#数据持久化练习
import sqlite3

#连接磁盘数据库
conn = sqlite3.connect("practice.db")

#创建订单表
conn.execute("""
CREATE TABLE IF NOT EXISTS orders(
    order_id TEXT PRIMARY KEY,
    amount INTEGER NOT NULL,
    status TEXT NOT NULL
)
""")

#插入一条测试订单
conn.execute(
    """
    INSERT OR IGNORE INTO orders
    (order_id, amount, status)
    VALUES (?, ?, ?)
    """,
    ("ORD-100", 500, "paid")
)
#提交事务并关闭连接
conn.commit()
conn.close()

print("数据库连接已关闭")


#重新连接同一个数据库文件
conn = sqlite3.connect("practice.db")


#查询刚刚保存的订单
cursor = conn.execute(
    """
    SELECT order_id, amount, status
    FROM orders
    WHERE order_id = ?
    """,
    ("ORD-100",)
)

order = cursor.fetchone()

print("重新连接后查询：", order)


#关闭连接
conn.close()