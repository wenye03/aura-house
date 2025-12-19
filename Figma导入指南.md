# HTML原型导入Figma指南

## 方法一：使用Figma插件（推荐）

### 1. HTML to Design插件
- 在Figma中搜索并安装 "HTML to Design" 插件
- 打开插件，输入你的HTML文件URL或直接粘贴HTML代码
- 插件会自动转换为Figma设计元素

### 2. html.to.design插件
- 安装 "html.to.design" 插件
- 支持直接导入HTML文件
- 可以保留基本的样式和布局

## 方法二：使用浏览器截图工具

### 1. Figma的截图导入
1. 在浏览器中打开你的HTML文件（如 `prototype-index.html`）
2. 使用浏览器开发者工具调整到合适的尺寸（iPhone 15 Pro: 393x852px）
3. 截图每个界面
4. 在Figma中：File → Place Image → 选择截图

### 2. 使用Figma的Capture插件
- 安装 "Capture" 插件
- 可以快速截取浏览器中的界面
- 自动导入到Figma画板

## 方法三：使用Figma插件（最推荐，最可靠）

### 1. html.to.design 插件（官方推荐）
**这是最可靠的方法！**

安装步骤：
1. 打开Figma桌面应用或网页版
2. 在画布上右键点击 → 选择 "Plugins" → "Browse plugins in Community"
3. 搜索 "html.to.design"
4. 点击 "Install" 安装

使用方法：
1. 在Figma中右键点击画布 → "Plugins" → "html.to.design"
2. 在插件界面中：
   - 如果HTML文件在本地：需要先启动本地服务器
   - 如果HTML已部署：直接输入URL
   - 也可以直接粘贴HTML代码
3. 点击 "Import" 开始转换
4. 转换完成后会在Figma中生成设计元素

### 2. HTML to Design 插件
- 搜索并安装 "HTML to Design"
- 支持导入HTML代码或URL
- 可以保留基本的样式和布局

### 3. Anima插件
- 安装Figma插件 "Anima"
- 支持从HTML/CSS直接生成Figma设计
- 可以保持响应式布局
- 支持代码到设计的双向转换

## 方法四：手动重建（最精确）

### 步骤：
1. **准备设计规范**
   - 记录所有颜色值（已在代码中使用）
   - 记录字体大小和行高
   - 记录间距和圆角值
   - 记录阴影效果

2. **在Figma中创建**
   - 创建iPhone 15 Pro画板（393x852px）
   - 使用Frame工具重建布局
   - 应用相同的颜色、字体、间距

3. **使用Figma的自动布局**
   - 利用Auto Layout功能快速构建
   - 保持与HTML相同的间距系统

## 方法五：使用设计令牌（Design Tokens）

### 提取设计令牌
从你的HTML代码中提取：

```javascript
// 颜色
const colors = {
  background: '#f5f5f7',
  card: 'rgba(255, 255, 255, 0.95)',
  text: {
    primary: '#1d1d1f',
    secondary: '#6e6e73',
    tertiary: '#86868b'
  },
  accent: '#007aff'
}

// 间距
const spacing = {
  xs: '4px',
  sm: '8px',
  md: '16px',
  lg: '24px',
  xl: '32px'
}

// 圆角
const borderRadius = {
  sm: '8px',
  md: '16px',
  lg: '24px',
  xl: '28px'
}
```

在Figma中创建这些变量，然后应用到设计中。

## 推荐工作流程

### 快速方案（适合快速预览）
1. 使用浏览器打开 `prototype-index.html`
2. 使用Figma的Capture插件截图
3. 导入到Figma画板

### 精确方案（适合最终设计）
1. 使用html.to.design插件转换（需要本地服务器）
2. 在Figma中手动调整细节
3. 使用设计令牌统一规范

### 专业方案（适合团队协作）
1. 提取设计令牌
2. 在Figma中创建组件库
3. 使用Auto Layout重建界面
4. 保持与HTML代码的一致性

## 注意事项

1. **字体**：确保Figma中安装了相同的字体（-apple-system, BlinkMacSystemFont等）
2. **毛玻璃效果**：Figma中的Backdrop Blur效果可能与CSS不完全一致，需要手动调整
3. **渐变**：检查渐变方向是否一致
4. **阴影**：Figma的阴影参数可能需要微调
5. **响应式**：HTML是响应式的，Figma中需要创建多个画板尺寸

## 工具推荐（按可靠性排序）

1. **html.to.design插件** ⭐⭐⭐⭐⭐ - Figma官方社区插件，最可靠
2. **HTML to Design插件** ⭐⭐⭐⭐ - 功能强大的转换插件
3. **Anima插件** ⭐⭐⭐⭐ - 支持双向转换
4. **Figma Capture插件** ⭐⭐⭐ - 快速截图导入
5. **手动重建** ⭐⭐⭐⭐⭐ - 最精确，但耗时较长

## 重要提示：本地HTML文件需要启动服务器

如果你的HTML文件在本地（如 `prototype-index.html`），插件无法直接访问本地文件。需要：

### 方法A：使用Python启动本地服务器（推荐）
```bash
# 在项目目录下运行
python -m http.server 8000
# 或使用Python 3
python3 -m http.server 8000
```
然后在浏览器访问 `http://localhost:8000/prototype-index.html`
在Figma插件中输入这个URL

### 方法B：使用Node.js的http-server
```bash
# 安装
npm install -g http-server

# 在项目目录下运行
http-server -p 8000
```

### 方法C：使用VS Code的Live Server插件
1. 在VS Code中安装 "Live Server" 插件
2. 右键点击HTML文件 → "Open with Live Server"
3. 会自动打开浏览器并显示本地URL

## 快速开始

最简单的步骤：
1. 在浏览器中打开 `prototype-index.html`
2. 按F12打开开发者工具
3. 使用设备模拟器设置为iPhone 15 Pro
4. 截图每个界面
5. 在Figma中创建画板并导入截图
6. 使用Figma的自动布局和组件功能重建

