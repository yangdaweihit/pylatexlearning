#!/usr/bin/env python3
"""
- subprocess.check_output测试
- 封装到compile函数之中
"""

import subprocess
import os
import sys


def compile(filenamepath):

    filenamepath = os.path.abspath(filenamepath)
    filepath, filename = os.path.split(filenamepath)

    main, ext = os.path.splitext(filename)

    if ext != '.tex':
        print("the extension of file {0} is not .tex.".format(ext))
        print("Game is over.")
        sys.exit(1)
    else:
        main_arguments = ['--interaction=nonstopmode', filenamepath]
        command = ['latexmk', '--xelatex'] + main_arguments
        check_output_kwargs = {'cwd': filepath}
        try:
            # output = subprocess.check_output(command,
            #                                  stderr=subprocess.STDOUT,
            #                                  **check_output_kwargs)
            subprocess.check_output(command,
                                    stderr=subprocess.STDOUT,
                                    **check_output_kwargs)
        except subprocess.CalledProcessError as e:
            print(e.output.decode())
        else:
            # print(output.decode())
            pass


if __name__ == '__main__':

    parnum = len(os.sys.argv)

    if parnum != 2:
        print("USAGE: python3 p008.py <tex> ")
    else:
        compile(os.sys.argv[1])
