#!/usr/bin/env python3
"""
文件统计工具

扫描指定目录，统计文件数量、类型分布和总大小。
"""

import os
import sys
from pathlib import Path
from collections import defaultdict


def scan_directory(directory_path):
    """
    扫描目录并收集文件信息
    
    Args:
        directory_path: 要扫描的目录路径
    
    Returns:
        tuple: (文件列表, 类型统计字典, 总大小)
    """
    if not os.path.isdir(directory_path):
        print(f"错误: '{directory_path}' 不是有效的目录")
        return [], {}, 0
    
    files = []
    type_stats = defaultdict(int) 
    total_size = 0
    
    for root, _, filenames in os.walk(directory_path):
        for filename in filenames:
            filepath = os.path.join(root, filename)
            try:
                size = os.path.getsize(filepath)
                files.append((filepath, size))
                total_size += size
                
                # 统计文件类型
                ext = os.path.splitext(filename)[1].lower()
                if ext:
                    type_stats[ext] += 1
                else:
                    type_stats["无扩展名"] += 1
            except (OSError, PermissionError):
                # 跳过无法访问的文件
                continue
    
    return files, dict(type_stats), total_size #返回文件列表、类型统计字典、总大小


def format_size(size_bytes):
    """将字节数格式化为易读的单位"""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.1f} PB"


def print_report(directory, files, type_stats, total_size):
    """打印统计报告"""
    print(f"扫描目录: {directory}")
    print(f"文件总数: {len(files)}")
    
    if type_stats:
        print("文件类型分布:")
        for ext, count in sorted(type_stats.items(), key=lambda x: x[1], reverse=True):
            print(f"  {ext}: {count} 个")
    
    print(f"总大小: {format_size(total_size)}")


def main():

    """主函数"""
    # 判断是否提供了命令行参数
    if len(sys.argv) >= 2:
        # 使用命令行参数
        directory = sys.argv[1]
    else:
        # 交互式输入
        print("文件统计工具")
        print("=" * 30)
        default_path = "."  # 默认当前目录
        user_input = input(f"请输入要扫描的目录路径 (默认: '{default_path}'，直接回车使用默认): ").strip()
        
        if user_input == "":
            directory = default_path
            print(f"使用默认路径: '{directory}'")
        else:
            directory = user_input
    
    # 验证目录是否存在
    if not os.path.isdir(directory):
        print(f"错误: '{directory}' 不是有效的目录")
        sys.exit(1)
    
    # 扫描目录
    files, type_stats, total_size = scan_directory(directory)
    
    if not files:
        print(f"目录 '{directory}' 中没有找到文件")
        sys.exit(0)
    
    # 打印报告
    print_report(directory, files, type_stats, total_size)


#如果脚本作为主程序运行（而不是被导入），则调用main函数
if __name__ == "__main__":
    main()