#SQLite数据表练习
import sqlite3

#1创建内存数据库连接
conn = sqlite3.connect("agent.db")

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

#3.1查询已创建表
cursor = conn.execute("""
SELECT name FROM sqlite_master
WHERE type = 'table'
""")

#3.2获取查询结果
tables = cursor.fetchall()
print("表",tables)

#3.3插入虚拟订单
conn.execute("""
    INSERT INTO orders (order_id,amount,status)
    VALUES(?,?,?)
    """,
    ("ORD-001",199,"paid")
)
conn.commit()
print("订单ORD-001插入成功")

#3.4查询订单
cursor = conn.execute(
    """
    SELECT order_id, amount, status
    FROM orders
    WHERE order_id = ?
    """,
    ("ORD-001",)
)
order = cursor.fetchone()
if order is not None:
    print("查询到订单：", order)
else:
    print("订单不存在")

#3.5update修改订单
cursor = conn.execute(
    """
UPDATE orders
SET status=?
WHERE order_id = ?
""",
("refunded","ORD-001")
)
conn.commit()
print("本次更新行数:",cursor.rowcount)

cursor = conn.execute(
    """
    SELECT order_id, amount, status
    FROM orders
    WHERE order_id = ?
    """,
    ("ORD-001",)
)

updated_order = cursor.fetchone()

print("更新后的订单：", updated_order)
# DELETE 删除数据
cursor = conn.execute(
    """
    DELETE FROM orders
    WHERE order_id = ?
    """,
    ("ORD-001",)
)

conn.commit()
print("本次删除行数：", cursor.rowcount)


cursor = conn.execute(
    """
    SELECT order_id, amount, status
    FROM orders
    WHERE order_id = ?
    """,
    ("ORD-001",)
)

deleted_order = cursor.fetchone()

print("删除后查询结果：", deleted_order)
#4关闭数据库
conn.close()