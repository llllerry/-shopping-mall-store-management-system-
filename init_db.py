# init_db.py
import mysql.connector

# 你也可以从 src/database.py 里 import 配置，这里写死是为了演示
config = {
    "host": "localhost",
    "user": "你的用户名",
    "password": "你的密码"
}

DB_NAME = "shop_management"

TABLES = {}
TABLES["shops"] = (
    """
    CREATE TABLE IF NOT EXISTS shops (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        type VARCHAR(50),
        revenue DECIMAL(10,2),
        manager VARCHAR(50),
        phone VARCHAR(20)
    )
    """
)

TABLES["users"] = (
    """
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(50) NOT NULL UNIQUE,
        password VARCHAR(100) NOT NULL,
        role ENUM('admin', 'user') DEFAULT 'user'
    )
    """
)


def create_database(cursor):
    try:
        cursor.execute(
            f"CREATE DATABASE {DB_NAME} DEFAULT CHARACTER SET 'utf8mb4'"
        )
        print(f"数据库 {DB_NAME} 创建成功！")
    except mysql.connector.Error as err:
        print(f"数据库创建失败: {err}")


def main():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    # 创建数据库
    try:
        conn.database = DB_NAME
    except mysql.connector.Error:
        create_database(cursor)
        conn.database = DB_NAME

    # 创建数据表
    for name, ddl in TABLES.items():
        try:
            cursor.execute(ddl)
            print(f"数据表 {name} 创建成功！")
        except mysql.connector.Error as err:
            print(f"创建表 {name} 失败: {err}")

    cursor.close()
    conn.close()
