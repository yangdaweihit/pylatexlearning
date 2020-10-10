#!/usr/bin/python
"""
生成片断示例
"""

from pylatex import Document, Section, Figure, Command, \
    Package, Table, Tabu, Label, MiniPage
from pylatex.utils import bold
import os

if __name__ == '__main__':

    table = Table(position='htpb')

    table.append(Command('centering'))
    # table.append(Command('caption', '外观检测'))
    table.add_caption("外观检测")
    table.append(Command('label', 'tbl:inspect'))

    tabu = Tabu("X[l] X[3,l]")

    # tabu.add_topline()
    tabu.add_row(["date", "description"], mapper=bold)
    tabu.add_hline()
    tabu.add_row(["2020-10-05", "meeting"])
    tabu.add_row(["2020-10-05", "meeting"])
    tabu.add_row(["2020-10-05", "meeting"])
    tabu.add_row(["2020-10-05", "meeting"])
    tabu.add_row(["2020-10-05", "meeting"])

    table.append(tabu)

    with open('p006.tex', 'w') as outfile:
        outfile.write(table.dumps())
