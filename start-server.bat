@echo off
chcp 65001 >nul
echo 正在启动本地服务器...
echo.
echo 服务器地址: http://localhost:8000
echo 主页面: http://localhost:8000/prototype-index.html
echo.
echo 按 Ctrl+C 停止服务器
echo.
cd /d "%~dp0"
python -m http.server 8000
pause

