# 店铺管理系统
# -shopping-mall-store-management-system-
A shop management system based on Python, Tkinter, MySQL and OpenCV
# 🏬 Shopping Mall Management System

一个基于 **Python (tkinter + MySQL)** 的简易商场管理系统。  
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
  - 使用 MyQSL 本地数据库  
  - 数据持久化保存  

- **界面设计**  
  - 基于 tkinter 的简洁图形界面  
  - 支持基本交互操作  

---
## 🤖 人脸识别模型文件

为控制仓库体积，模型文件不随代码提交。请手动放置到 `models/` 目录（需自行下载）：

- `shape_predictor_68_face_landmarks.dat`（由于无法上传大于25m的文件，so放个网盘链接吧通过网盘分享的文件：shape_predictor_68_face_landmarks.dat
链接: https://pan.baidu.com/s/1M4XEx3pINshHtFQZ-YWxEQ?pwd=1212 提取码: 1212）
- `dlib_face_recognition_resnet_model_v1.dat`

步骤：
1. 在项目根目录创建 `models/`（仓库已含占位文件也可）。
2. 将上述两个 `.dat` 文件拷入 `models/`。
3. 运行 `python main.py`。程序会自动检测；若未找到，会弹出文件选择框让你定位文件路径。

## 📂 项目结构
```text
shop-management/
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
