#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HTML文件优化脚本 - 用于Figma导入
移除外部CDN依赖，内联所有样式，替换图标
"""

import re
import os

# Font Awesome图标到Emoji的映射
ICON_MAP = {
    'fa-home': '🏠',
    'fa-th-large': '📱',
    'fa-magic': '🎭',
    'fa-store': '🛒',
    'fa-cog': '⚙️',
    'fa-bars': '☰',
    'fa-bell': '🔔',
    'fa-search': '🔍',
    'fa-lightbulb': '💡',
    'fa-clock': '⏰',
    'fa-wifi': '📶',
    'fa-thermometer-half': '🌡️',
    'fa-tv': '📺',
    'fa-snowflake': '❄️',
    'fa-broom': '🧹',
    'fa-backward': '⏮️',
    'fa-play': '▶️',
    'fa-forward': '⏭️',
    'fa-heart': '❤️',
    'fa-arrow-left': '←',
    'fa-ellipsis-v': '⋮',
    'fa-minus': '−',
    'fa-plus': '+',
    'fa-sun': '☀️',
    'fa-moon': '🌙',
    'fa-music': '🎵',
    'fa-edit': '✏️',
    'fa-trash': '🗑️',
    'fa-chevron-right': '→',
}

def replace_icons(html_content):
    """替换Font Awesome图标为Emoji"""
    # 匹配 <i class="fas fa-xxx"> 或 <i class="fas fa-xxx text-xxx">
    pattern = r'<i class="fas\s+([^"]+)"></i>'
    
    def replace_icon(match):
        classes = match.group(1).split()
        for icon_class in classes:
            if icon_class.startswith('fa-'):
                icon_name = icon_class
                if icon_name in ICON_MAP:
                    return ICON_MAP[icon_name]
        return match.group(0)
    
    html_content = re.sub(pattern, replace_icon, html_content)
    return html_content

def remove_external_deps(html_content):
    """移除外部CDN依赖"""
    # 移除Tailwind CDN
    html_content = re.sub(r'<script src="https://cdn\.tailwindcss\.com"></script>\s*', '', html_content)
    # 移除Font Awesome CDN
    html_content = re.sub(r'<link rel="stylesheet" href="https://cdnjs\.cloudflare\.com/ajax/libs/font-awesome/[^"]+">\s*', '', html_content)
    return html_content

def replace_backdrop_filter(html_content):
    """替换backdrop-filter为纯色背景"""
    # 将backdrop-filter改为纯色背景
    html_content = re.sub(r'backdrop-filter:\s*blur\([^)]+\)\s*saturate\([^)]+\);', '', html_content)
    # 将半透明背景改为更不透明的背景
    html_content = re.sub(r'rgba\(255,\s*255,\s*255,\s*0\.7\)', 'rgba(255, 255, 255, 0.95)', html_content)
    html_content = re.sub(r'rgba\(255,\s*255,\s*255,\s*0\.8\)', 'rgba(255, 255, 255, 0.95)', html_content)
    return html_content

def optimize_html_file(filepath):
    """优化单个HTML文件"""
    print(f"正在优化: {filepath}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 执行优化
    content = remove_external_deps(content)
    content = replace_icons(content)
    content = replace_backdrop_filter(content)
    
    # 保存优化后的文件（添加-figma后缀）
    output_path = filepath.replace('.html', '-figma.html')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"已保存: {output_path}")

if __name__ == '__main__':
    # 需要优化的文件列表
    files_to_optimize = [
        'home.html',
        'device-light.html',
        'device-air.html',
        'device-temp.html',
        'devices.html',
        'rooms.html',
        'scenes.html',
        'shop.html',
        'profile.html',
        'outdoor.html',
    ]
    
    for filename in files_to_optimize:
        if os.path.exists(filename):
            try:
                optimize_html_file(filename)
            except Exception as e:
                print(f"处理 {filename} 时出错: {e}")
        else:
            print(f"文件不存在: {filename}")

