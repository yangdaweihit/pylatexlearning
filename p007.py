#!/usr/bin/env python3
"""
os.path
"""

import os

if __name__ == '__main__':

    print("__file__: ", __file__)
    print("basename: ", os.path.basename(__file__))
    abspath = os.path.abspath(__file__)
    print("total path: ", abspath)
    print("directory path: ", os.path.dirname(abspath))
    print("current path: ", os.getcwd())

    # 把路径分割成 dirname 和 basename，返回一个元组
    filepath, filename = os.path.split(abspath)
    print((filepath, filename))

    # 分割路径，返回路径名和文件扩展名的元组
    print(os.path.splitext(abspath))

    # 进入文件所在目录
    os.chdir(filepath)
    print("current path: ", os.getcwd())
