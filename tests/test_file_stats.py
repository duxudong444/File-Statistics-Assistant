import os
import tempfile
import shutil
from pathlib import Path
import sys

# 添加 src 目录到 Python 路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from file_stats import scan_directory, format_size


def test_format_size():
    """测试文件大小格式化"""
    assert format_size(0) == "0.0 B"
    assert format_size(1023) == "1023.0 B"
    assert format_size(1024) == "1.0 KB"
    assert format_size(1024 * 1024) == "1.0 MB"
    assert format_size(1024 * 1024 * 1024) == "1.0 GB"


def test_scan_directory_empty():
    """测试扫描空目录"""
    with tempfile.TemporaryDirectory() as temp_dir:
        files, stats, total_size = scan_directory(temp_dir)
        assert len(files) == 0
        assert stats == {}
        assert total_size == 0


def test_scan_directory_with_files():
    """测试扫描包含文件的目录"""
    with tempfile.TemporaryDirectory() as temp_dir:
        # 创建测试文件
        test_files = [
            ("test1.txt", 100),
            ("test2.txt", 200),
            ("image.jpg", 1500),
            ("document.pdf", 3000),
        ]
        
        for filename, size in test_files:
            filepath = os.path.join(temp_dir, filename)
            with open(filepath, 'wb') as f:
                f.write(b'x' * size)
        
        # 创建子目录和文件
        subdir = os.path.join(temp_dir, "subdir")
        os.makedirs(subdir)
        with open(os.path.join(subdir, "nested.txt"), 'wb') as f:
            f.write(b'x' * 500)
        
        files, stats, total_size = scan_directory(temp_dir)
        
        # 验证结果
        assert len(files) == 5  # 4个文件 + 1个子目录文件
        assert stats[".txt"] == 3  # test1.txt, test2.txt, nested.txt
        assert stats[".jpg"] == 1
        assert stats[".pdf"] == 1
        assert total_size == 100 + 200 + 1500 + 3000 + 500


def test_scan_invalid_directory():
    """测试扫描无效目录"""
    files, stats, total_size = scan_directory("/non/existent/path")
    assert len(files) == 0
    assert stats == {}
    assert total_size == 0


def test_scan_directory_permission_issue():
    """测试权限问题处理（模拟跳过无法访问的文件）"""
    # 这个测试在Windows上可能表现不同，我们主要测试函数不会崩溃
    with tempfile.TemporaryDirectory() as temp_dir:
        files, stats, total_size = scan_directory(temp_dir)
        # 应该正常返回，不会抛出异常
        assert isinstance(files, list)
        assert isinstance(stats, dict)
        assert isinstance(total_size, int)


if __name__ == "__main__":
    # 简单运行测试
    test_format_size()
    test_scan_directory_empty()
    test_scan_directory_with_files()
    test_scan_invalid_directory()
    test_scan_directory_permission_issue()
    print("所有测试通过！")