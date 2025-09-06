# src/database.py
import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='你的密码',
        database='shop_management'
    )

def get_user_by_username(username):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user

def add_shop(shop_data):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO shops (name, type, revenue, manager, contact) VALUES (%s,%s,%s,%s,%s)",
        (shop_data['name'], shop_data['type'], shop_data['revenue'], shop_data['manager'], shop_data['contact'])
    )
    conn.commit()
    cursor.close()
    conn.close()
