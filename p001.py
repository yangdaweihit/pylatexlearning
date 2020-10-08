#!/usr/bin/env python3
"""
本例测试了PyLaTeX如下功能：

- NoEscape
- Commmand
- Document
- Figure
- Tabu
- LongTabu

"""

import os
from pylatex import Document, Section, Command, \
    Figure, Package, Label, Ref, Tabu, MiniPage, \
    LineBreak, LongTabu, MultiColumn
from pylatex.utils import NoEscape, bold

geometry_options = {
    "head": "40pt",
    "margin": "0.5in",
    "bottom": "0.6in"
    # "includedfoot": False
}

# doc = Document('p001',
#                geometry_options=geometry_options)

doc = Document('p001', documentclass='hitec')

# 加入宏包
doc.packages.append(Package('ctex', options=r'UTF8'))

# 导言区内容
doc.preamble.append(Command('title', 'PyLaTeX测试'))
doc.preamble.append(Command('author', '哈尔滨合正科技'))
doc.preamble.append(Command('date', NoEscape(r'\today')))
doc.append(NoEscape(r'\maketitle'))
# 正文
# doc.append(Command('input', 'sec1.tex'))

# 插入tex原文
with open('plaintext.tex') as infile:
    for line in infile:
        doc.append(NoEscape(line))

with doc.create(Section('插图')):

    # 插图
    with doc.create(Figure(position='htpb')) as logo:
        logo_file = os.path.join(os.path.dirname(__file__), 'logo.png')
        logo.add_image(logo_file, width=NoEscape(r'0.2\textwidth'))
        logo.add_caption('logo of hit')
        logo.append(Label('fig:hitlogo'))

    doc.extend(['如图', Ref('fig:hitlogo'), '所示'])
    doc.append(Command('vskip1em'))

with doc.create(Section('Tabu表格')):

    # 插入tabu表格
    with doc.create(Tabu("X[l] X[r]")) as first_page_table:
        customer = MiniPage(width=NoEscape(r"0.49\textwidth"), pos='h')
        customer.append("Verna Volcano")
        customer.append("\n")
        customer.append("For some Person")
        customer.append("\n")
        customer.append("Address1")
        customer.append("\n")
        customer.append("Address2")
        customer.append("\n")
        customer.append("Address3")

        # Add branch information
        branch = MiniPage(width=NoEscape(r"0.49\textwidth"),
                          pos='t!',
                          align='r')
        branch.append("Branch no.")
        branch.append(LineBreak())
        branch.append(bold("1181..."))
        branch.append(LineBreak())
        branch.append(bold("TIB Cheque"))

        first_page_table.add_row([customer, branch])
        first_page_table.add_empty_row()

with doc.create(Section('LongTabu表格')):

    with doc.create(
            LongTabu(" X[l]  X[l]  X[r]  X[r]  X[r] ",
                     row_height=1.5,
                     booktabs=True)) as data_table:

        data_table.append(Command('caption', '数据'))
        data_table.append(Command('label', 'Tab:1'))
        data_table.append(NoEscape(r'\\'))
        # data_table.add_hline()
        data_table.add_topline()

        data_table.add_row(
            ["date", "description", "debits($)", "credits($)", "balance($)"],
            mapper=bold,
            color="lightgray")
        data_table.add_hline()
        data_table.append(Command(r'endfirsthead'))

        data_table.append(Command('caption', '数据(续表)'))
        data_table.append(NoEscape(r'\\'))
        # data_table.add_hline()

        data_table.add_topline()
        data_table.add_row(
            ["date", "description", "debits($)", "credits($)", "balance($)"],
            mapper=bold,
            color="lightgray")
        data_table.add_hline()

        data_table.end_table_header()

        # data_table.add_hline()
        data_table.add_bottomline()
        data_table.add_row((MultiColumn(5, align='r', data='续表见下页'), ))
        # data_table.add_hline()
        data_table.end_table_footer()

        # data_table.add_hline()
        # data_table.add_row((MultiColumn(3, align='r',
        #                     data='Not Continued on Next Page'),))
        # data_table.add_hline()
        data_table.end_table_last_footer()

        row = ["2016-JUN-01", "Test", "$100", "$1000", "-$900"]
        for i in range(30):
            if (i % 2) == 0:
                data_table.add_row(row, color="lightgray")
            else:
                data_table.add_row(row)

            # data_table.add_hline()

        data_table.add_bottomline()

# 仅生成tex文档
# doc.generate_tex()

# 生成pdf文件
doc.generate_pdf(compiler='latexmk',
                 compiler_args=['-xelatex'],
                 clean_tex=False)
# doc.generate_pdf(clean_tex=False)
