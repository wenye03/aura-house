# URL问题排查指南

## 🔍 常见问题

### 问题1：Figma插件无法访问本地URL

**症状**：在Figma插件中粘贴URL后，提示无法访问或连接失败

**原因**：某些Figma插件可能无法直接访问本地服务器（localhost或127.0.0.1）

**解决方案**：

#### 方案A：使用本地文件路径（推荐）
1. 在Figma插件中选择 "Import from File" 或 "Import HTML File"
2. 直接选择HTML文件（如 `home.html`）
3. 插件会直接读取文件内容

#### 方案B：使用内网IP地址
1. 查找你的本机IP地址：
   ```powershell
   ipconfig
   ```
   找到 "IPv4 地址"，例如：`192.168.1.100`

2. 修改URL为：
   ```
   http://192.168.1.100:8000/home.html
   ```

3. 确保防火墙允许8000端口访问

#### 方案C：使用ngrok等内网穿透工具
1. 下载ngrok：https://ngrok.com/
2. 启动本地服务器后，运行：
   ```bash
   ngrok http 8000
   ```
3. 使用ngrok提供的公网URL（如：`https://xxxx.ngrok.io/home.html`）

### 问题2：URL格式不正确

**正确的URL格式**：
- ✅ `http://127.0.0.1:8000/home.html`
- ✅ `http://localhost:8000/home.html`
- ❌ `file:///E:/STUDY/Works/毕设/home.html`（Figma插件不支持）

### 问题3：服务器未启动

**检查方法**：
1. 打开浏览器，访问：`http://127.0.0.1:8000/test-all-pages.html`
2. 如果无法访问，说明服务器未启动
3. 双击 `start-server.bat` 启动服务器

### 问题4：端口被占用

**检查方法**：
```powershell
netstat -ano | findstr :8000
```

**解决方法**：
1. 如果端口被占用，修改 `start-server.bat` 中的端口号（如改为8001）
2. 同时更新所有URL中的端口号

## 🎯 推荐解决方案

### 最佳方案：直接导入HTML文件

大多数Figma插件（如 `html.to.design`）支持直接导入HTML文件：

1. **在Figma中**：
   - 右键点击画布 → Plugins → html.to.design
   - 选择 "Import from File" 或 "Browse"
   - 直接选择项目文件夹中的HTML文件（如 `home.html`）

2. **优点**：
   - ✅ 不需要启动服务器
   - ✅ 不需要URL
   - ✅ 更简单直接
   - ✅ 不受网络限制

3. **注意事项**：
   - 确保HTML文件中的外部资源（CSS、JS）使用CDN链接
   - 图片链接使用在线URL（如Unsplash）

## 📝 所有界面文件列表

如果使用文件导入方式，直接选择以下文件：

1. `home.html` - 首页
2. `device-light.html` - 智能灯光
3. `device-air.html` - 空气净化器
4. `device-temp.html` - 温度控制
5. `devices.html` - 设备管理
6. `rooms.html` - 房间列表
7. `scenes.html` - 场景管理
8. `shop.html` - 商城
9. `profile.html` - 个人中心
10. `outdoor.html` - 户外天气

## 🔧 快速测试

### 测试服务器是否正常：
1. 启动服务器（双击 `start-server.bat`）
2. 在浏览器中打开：`http://127.0.0.1:8000/test-all-pages.html`
3. 点击任意"打开"按钮，确认界面正常显示

### 测试URL是否可用：
1. 在浏览器地址栏输入：`http://127.0.0.1:8000/home.html`
2. 如果正常显示，说明URL可用
3. 如果无法显示，检查服务器是否启动

## 💡 提示

- 如果Figma插件支持文件导入，**优先使用文件导入方式**，更简单可靠
- 如果必须使用URL，确保服务器正在运行
- 使用 `127.0.0.1` 比 `localhost` 更可靠
- 如果遇到问题，尝试重启服务器

