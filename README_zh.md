![NotingDownCover](README.assets/NotingDownCover.png)

## 简介

一款截图与文档图像增强软件，旨在提供一种**轻松捕获和增强图像的方式**，适用于课堂、会议和其他场合的笔记记录。软件包括诸如**屏幕截图、图像二值化（可选保留颜色）和透视校正**等功能。软件使用Python编写，使用PyQt5 GUI库，与Windows和Linux操作系统兼容。

## 特点

- **截图功能**：用户可以截取全屏、单个窗口或选定区域的屏幕截图。
- **图像处理**：用户可以应用各种图像处理技术，如**屏幕截图、图像二值化（可选保留颜色）和透视校正**等。
- **快捷键**：用户可以使用快捷键快速截图并开始处理图像。

## 安装

### 要求

需要Python 3.8或更高版本

```
numpy==1.21.5
opencv_python==4.6.0.66
Pillow==9.5.0
PyQt5==5.15.9
system_hotkey==1.0.3
```

### 安装步骤

1. 克隆仓库并打开为工作路径
```bash
git clone https://github.com/MasterYip/NotingDown.git
cd ./NotingDown
```

2. 安装所需的软件包
```bash
pip install -r requirements.txt
```

3. 运行应用程序
```bash
python main.py
```

## 用法

1. 使用热键 `Alt+Q` 来截取屏幕截图。
2. 使用热键 `Ctrl+Alt+C` 处理您剪贴板中的图像，系统托盘中的图标将指示进度。
3. 使用热键 `Ctrl+Alt+F` 处理所选文件夹中的图像。
4. 双击图标调整主面板中的设置。

## 许可证

该项目基于 MIT 许可证发布 - 请参阅 LICENSE 文件了解详情。

## 贡献者

- [Master Yip](https://github.com/MasterYip)