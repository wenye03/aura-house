# 启动本地服务器脚本
Write-Host "正在启动本地服务器..." -ForegroundColor Green
Write-Host ""
Write-Host "服务器地址: http://localhost:8000" -ForegroundColor Cyan
Write-Host "主页面: http://localhost:8000/prototype-index.html" -ForegroundColor Cyan
Write-Host ""
Write-Host "按 Ctrl+C 停止服务器" -ForegroundColor Yellow
Write-Host ""

# 获取脚本所在目录
$scriptPath = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptPath

# 尝试使用Python启动服务器
try {
    python -m http.server 8000
} catch {
    Write-Host "Python不可用，尝试使用python3..." -ForegroundColor Yellow
    try {
        python3 -m http.server 8000
    } catch {
        Write-Host "错误: 未找到Python，请先安装Python" -ForegroundColor Red
        Write-Host "下载地址: https://www.python.org/downloads/" -ForegroundColor Yellow
        pause
    }
}

