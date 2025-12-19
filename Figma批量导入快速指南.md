# Figma批量导入快速指南

## 🚀 三步快速开始

### 第一步：启动服务器
双击运行 `start-server.bat` 文件

### 第二步：测试所有界面
在浏览器中打开：
```
http://localhost:8000/test-all-pages.html
```

这个页面会显示所有10个界面，你可以：
- ✅ 点击"打开"按钮测试每个界面
- ✅ 点击"复制URL"按钮复制URL到剪贴板

### 第三步：在Figma中导入

1. **安装插件**
   - 打开Figma
   - 右键点击画布 → Plugins → Browse plugins in Community
   - 搜索 "html.to.design"
   - 点击 Install

2. **导入界面**
   - 右键点击画布 → Plugins → html.to.design
   - 在插件中选择 "Import from URL"
   - 粘贴复制的URL（从test-all-pages.html页面复制）
   - 点击 Import
   - 等待转换完成

3. **重复导入**
   - 重复步骤2，导入所有10个界面
   - 每个界面导入后，重命名为有意义的名称

## 📋 所有界面列表

| 序号 | 界面名称 | URL |
|------|---------|-----|
| 1 | 首页 | `http://localhost:8000/home.html` |
| 2 | 智能灯光 | `http://localhost:8000/device-light.html` |
| 3 | 空气净化器 | `http://localhost:8000/device-air.html` |
| 4 | 温度控制 | `http://localhost:8000/device-temp.html` |
| 5 | 设备管理 | `http://localhost:8000/devices.html` |
| 6 | 房间列表 | `http://localhost:8000/rooms.html` |
| 7 | 场景管理 | `http://localhost:8000/scenes.html` |
| 8 | 商城 | `http://localhost:8000/shop.html` |
| 9 | 个人中心 | `http://localhost:8000/profile.html` |
| 10 | 户外天气 | `http://localhost:8000/outdoor.html` |

## 🎯 推荐工作流程

### 方案A：使用测试页面（最简单）
1. 打开 `http://localhost:8000/test-all-pages.html`
2. 逐个点击"复制URL"
3. 在Figma插件中粘贴并导入
4. 重复直到导入所有界面

### 方案B：直接复制URL列表
1. 打开 `批量导入URL列表.txt`
2. 复制每个URL
3. 在Figma插件中导入

## ⚡ 快速操作技巧

### 在Figma中组织界面

导入后建议这样组织：

```
📁 智能家居App
├── 📄 01-首页
│   └── home.html (已导入)
├── 📄 02-设备控制
│   ├── device-light.html
│   ├── device-air.html
│   ├── device-temp.html
│   └── devices.html
├── 📄 03-房间和场景
│   ├── rooms.html
│   └── scenes.html
├── 📄 04-商城
│   └── shop.html
└── 📄 05-个人中心
    ├── profile.html
    └── outdoor.html
```

### 导入后立即做的优化

1. **重命名Frame**
   - 给每个导入的界面Frame起个清晰的名字

2. **设置画板尺寸**
   - 统一设置为 393×852px（iPhone 15 Pro）

3. **创建组件**
   - 将重复的元素（按钮、卡片）转换为Component

4. **统一样式**
   - 创建Color Styles
   - 创建Text Styles

## ⏱️ 时间估算

- 单个界面导入：2-3分钟
- 10个界面总计：20-30分钟
- 整理和优化：30-60分钟
- **总计：约1-2小时**

## ❓ 常见问题

### Q: 导入后样式不对？
A: 某些CSS效果（如backdrop-blur）可能需要手动调整

### Q: 图片显示不出来？
A: 确保网络连接正常，Unsplash图片需要联网加载

### Q: 文字无法编辑？
A: 检查是否转换为Text元素，某些插件可能需要手动转换

### Q: 布局错乱？
A: 使用Figma的Auto Layout功能重新整理布局

## 💡 提示

- 💡 建议分批导入，避免一次性导入太多
- 💡 导入后立即保存Figma文件
- 💡 使用Figma的版本历史功能
- 💡 可以邀请团队成员协作编辑

## 🎉 完成！

导入完成后，你就可以在Figma中：
- ✅ 编辑所有文字和元素
- ✅ 修改颜色和样式
- ✅ 调整布局
- ✅ 创建交互原型
- ✅ 导出设计资源

