# src/main.py
import tkinter as tk
from ui import start_app

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Shopping Mall Management System")
    root.geometry("800x600")
    
    start_app(root)  # 启动应用（登录 -> 主界面）
    
    root.mainloop()
