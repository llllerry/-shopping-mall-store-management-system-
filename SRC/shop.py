# src/shop.py
import tkinter as tk
from database import add_shop

class ShopWindow:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(master)
        self.frame.pack(pady=20)
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.frame, text="店铺名称").grid(row=0, column=0)
        tk.Label(self.frame, text="类型").grid(row=1, column=0)
        tk.Label(self.frame, text="营业额").grid(row=2, column=0)
        tk.Label(self.frame, text="负责人").grid(row=3, column=0)
        tk.Label(self.frame, text="联系方式").grid(row=4, column=0)

        self.entries = [tk.Entry(self.frame) for _ in range(5)]
        for i, e in enumerate(self.entries):
            e.grid(row=i, column=1)

        tk.Button(self.frame, text="添加店铺", command=self.add_shop).grid(row=5, columnspan=2)

    def add_shop(self):
        data = {
            'name': self.entries[0].get(),
            'type': self.entries[1].get(),
            'revenue': self.entries[2].get(),
            'manager': self.entries[3].get(),
            'contact': self.entries[4].get()
        }
        add_shop(data)
        tk.Label(self.frame, text="添加成功！", fg="green").grid(row=6, columnspan=2)
