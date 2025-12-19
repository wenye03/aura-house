# 批量导入所有界面到Figma - 完整指南

## 方法一：使用插件逐个导入（推荐，最精确）

### 优点：
- ✅ 每个界面都是独立的，可以单独编辑
- ✅ 转换质量最好
- ✅ 可以按需导入

### 步骤：

1. **启动服务器**
   - 双击 `start-server.bat`

2. **在Figma中准备**
   - 创建新文件或打开现有文件
   - 安装 "html.to.design" 插件

3. **逐个导入界面**
   
   使用插件导入以下所有界面：
   
   ```
   http://localhost:8000/home.html
   http://localhost:8000/device-light.html
   http://localhost:8000/device-air.html
   http://localhost:8000/device-temp.html
   http://localhost:8000/devices.html
   http://localhost:8000/rooms.html
   http://localhost:8000/scenes.html
   http://localhost:8000/shop.html
   http://localhost:8000/profile.html
   http://localhost:8000/outdoor.html
   ```

4. **组织画板**
   - 每个界面导入后，重命名Frame
   - 使用画板（Frames）组织所有界面
   - 可以创建页面（Pages）分类管理

## 方法二：创建批量导入页面（快速预览）

### 创建一个包含所有界面的预览页面

我已经创建了 `prototype-index.html`，它使用iframe展示所有界面。

### 导入方式：

1. **导入主页面**
   ```
   http://localhost:8000/prototype-index.html
   ```
   - 这会导入整个预览页面
   - 但iframe内的内容可能无法直接编辑

2. **更好的方法**：导入每个iframe的源文件
   - 插件可能无法解析iframe
   - 建议使用方法一逐个导入

## 方法三：使用Figma的批量导入功能

### 如果插件支持批量导入：

1. **准备URL列表**
   创建一个文本文件，包含所有URL：
   ```
   http://localhost:8000/home.html
   http://localhost:8000/device-light.html
   http://localhost:8000/device-air.html
   http://localhost:8000/device-temp.html
   http://localhost:8000/devices.html
   http://localhost:8000/rooms.html
   http://localhost:8000/scenes.html
   http://localhost:8000/shop.html
   http://localhost:8000/profile.html
   http://localhost:8000/outdoor.html
   ```

2. **使用插件**
   - 某些插件支持批量导入
   - 查看插件说明是否支持

## 方法四：创建Figma文件结构（推荐工作流程）

### 在Figma中组织所有界面：

1. **创建页面结构**
   ```
   📁 智能家居App
   ├── 📄 首页
   │   └── home.html
   ├── 📄 设备控制
   │   ├── device-light.html
   │   ├── device-air.html
   │   ├── device-temp.html
   │   └── devices.html
   ├── 📄 房间和场景
   │   ├── rooms.html
   │   └── scenes.html
   ├── 📄 商城
   │   └── shop.html
   └── 📄 个人中心
       ├── profile.html
       └── outdoor.html
   ```

2. **导入步骤**
   - 在Figma中创建对应的Pages
   - 在每个Page中导入对应的界面
   - 使用命名规范：如"01-首页"、"02-设备控制"等

## 快速导入清单

### 所有界面列表（按顺序导入）：

| 序号 | 界面名称 | URL | 说明 |
|------|---------|-----|------|
| 1 | 首页 | `http://localhost:8000/home.html` | 主界面 |
| 2 | 智能灯光 | `http://localhost:8000/device-light.html` | 灯光控制 |
| 3 | 空气净化器 | `http://localhost:8000/device-air.html` | 净化器控制 |
| 4 | 温度控制 | `http://localhost:8000/device-temp.html` | 温度调节 |
| 5 | 设备管理 | `http://localhost:8000/devices.html` | 所有设备 |
| 6 | 房间列表 | `http://localhost:8000/rooms.html` | 房间管理 |
| 7 | 场景管理 | `http://localhost:8000/scenes.html` | 场景设置 |
| 8 | 商城 | `http://localhost:8000/shop.html` | 设备商城 |
| 9 | 个人中心 | `http://localhost:8000/profile.html` | 用户设置 |
| 10 | 户外天气 | `http://localhost:8000/outdoor.html` | 天气信息 |

## 导入后的优化建议

### 1. 统一设计系统
- 创建颜色样式（Color Styles）
- 创建文字样式（Text Styles）
- 创建效果样式（Effect Styles）

### 2. 创建组件库
- 将重复元素转换为组件（Components）
- 如：按钮、卡片、输入框等
- 方便后续维护和修改

### 3. 设置画板尺寸
- 所有界面统一使用：393×852px（iPhone 15 Pro）
- 或创建响应式画板

### 4. 添加交互原型
- 使用Figma的Prototype功能
- 连接各个界面
- 创建可点击的原型

## 自动化脚本（高级）

### 如果熟悉编程，可以创建脚本：

```javascript
// 批量导入脚本示例（需要配合Figma插件API）
const urls = [
  'http://localhost:8000/home.html',
  'http://localhost:8000/device-light.html',
  // ... 其他URL
];

// 使用Figma插件API批量导入
```

## 推荐工作流程

### 最佳实践：

1. **准备阶段**
   - ✅ 启动服务器
   - ✅ 测试所有页面都能正常访问
   - ✅ 在Figma中创建文件结构

2. **导入阶段**
   - ✅ 按功能模块分组导入
   - ✅ 每次导入后检查转换质量
   - ✅ 立即重命名和组织图层

3. **优化阶段**
   - ✅ 统一设计规范
   - ✅ 创建组件库
   - ✅ 添加交互原型

## 时间估算

- 单个界面导入：2-5分钟
- 10个界面总计：20-50分钟
- 优化和整理：30-60分钟
- **总计：约1-2小时**

## 提示

- 💡 建议分批导入，避免一次性导入太多
- 💡 导入后立即保存Figma文件
- 💡 可以邀请团队成员协作编辑
- 💡 使用Figma的版本历史功能

## 如果遇到问题

1. **导入失败**：检查服务器是否运行
2. **样式丢失**：某些CSS可能需要手动调整
3. **图片缺失**：检查网络连接，Unsplash图片需要联网
4. **布局错乱**：使用Figma的Auto Layout重新整理

