# -shopping-mall-store-management-system-
A shop management system based on Python, Tkinter, MySQL and OpenCV
# 🏬 Shopping Mall Management System

一个基于 **Python (tkinter + SQLite)** 的简易商场管理系统。  
本项目旨在提供一个完整的商场人员与店铺管理解决方案，包括 **登录认证、数据管理、可视化界面** 等功能。

---

## ✨ 功能特性
- **用户登录**  
  - 支持账号密码登录  
  - 简单权限管理（管理员 / 普通用户）

- **店铺管理**  
  - 添加 / 删除 / 修改 / 查询店铺信息  
  - 信息包括：店铺名称、类型、营业额、负责人及联系方式等  

- **数据库支持**  
  - 使用 SQLite 本地数据库  
  - 数据持久化保存  

- **界面设计**  
  - 基于 tkinter 的简洁图形界面  
  - 支持基本交互操作  

---

## 📂 项目结构
```shop-management/
├── main.py              # 程序入口，运行后启动界面
├── db/
│   └── shop.db          # SQLite 数据库文件
├── src/
│   ├── login.py         # 登录与注册模块
│   ├── shop.py          # 店铺管理模块（增删改查）
│   ├── face_recog.py    # 人脸识别模块（OpenCV + Dlib）
│   └── utils.py         # 工具函数（数据库连接、通用方法）
├── assets/
│   └── logo.png         # 界面图片或图标
├── requirements.txt     # 依赖库说明（如 tkinter、opencv、dlib 等）
└── README.md            # 项目说明文件
```
