# src/ui.py
import tkinter as tk
from auth import verify_login
from shop import ShopWindow

def start_app(root):
    login_frame = tk.Frame(root)
    login_frame.pack(pady=50)

    tk.Label(login_frame, text="用户名").grid(row=0, column=0)
    tk.Label(login_frame, text="密码").grid(row=1, column=0)
    username_entry = tk.Entry(login_frame)
    password_entry = tk.Entry(login_frame, show="*")
    username_entry.grid(row=0, column=1)
    password_entry.grid(row=1, column=1)

    def login_action():
        username = username_entry.get()
        password = password_entry.get()
        if verify_login(username, password):
            login_frame.destroy()
            ShopWindow(root)
        else:
            tk.Label(login_frame, text="登录失败", fg="red").grid(row=3, columnspan=2)

    tk.Button(login_frame, text="登录", command=login_action).grid(row=2, columnspan=2)
