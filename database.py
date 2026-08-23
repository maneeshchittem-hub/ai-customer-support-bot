import sqlite3

DB_NAME = "orders.db"


def create_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            order_id TEXT PRIMARY KEY,
            customer_name TEXT NOT NULL,
            product TEXT NOT NULL,
            status TEXT NOT NULL,
            estimated_delivery TEXT NOT NULL
        )
    """)

    orders = [
        ("ORD1001", "Maneesh", "Laptop", "Shipped", "August 20, 2026"),
        ("ORD1002", "Rahul", "Headphones", "Out for Delivery", "August 16, 2026"),
        ("ORD1003", "Priya", "Smart Watch", "Processing", "August 22, 2026"),
        ("ORD1004", "Arjun", "Keyboard", "Delivered", "August 14, 2026")
    ]

    cursor.executemany("""
        INSERT OR IGNORE INTO orders
        VALUES (?, ?, ?, ?, ?)
    """, orders)

    conn.commit()
    conn.close()


def get_order(order_id):

    create_database()

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT order_id,
               customer_name,
               product,
               status,
               estimated_delivery
        FROM orders
        WHERE order_id = ?
    """, (order_id,))

    order = cursor.fetchone()

    conn.close()

    return order