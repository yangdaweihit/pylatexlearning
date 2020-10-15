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
    LineBreak, LongTabu, MultiColumn, \
    PageStyle, Head, Foot
# from pylatex.section import Chapter
from pylatex.section import Chapter
from pylatex.utils import NoEscape, bold

geometry_options = {
    "head": "3cm",
    "margin": "3cm",
    "bottom": "3cm"
    # "includedfoot": False
}

doc = Document('p001',
               documentclass='report',
               geometry_options=geometry_options)

# 加入宏包
doc.packages.append(Package('ctex', options=r'UTF8'))
doc.packages.append(Package('booktabs'))
doc.packages.append(Package('caption'))

# 导言区内容
doc.preamble.append(Command('title', 'PyLaTeX测试'))
doc.preamble.append(Command('author', '哈尔滨合正科技'))
doc.preamble.append(Command('date', NoEscape(r'\today')))

header = PageStyle("header")
with header.create(Head("L")):
    header.append("自动报告示例")

with header.create(Head("R")):
    header.append("哈尔滨合正科技")

header.change_thickness('header', 1)

with header.create(Foot("C")):
    header.append(NoEscape(r'\thepage\ / \pageref{LastPage}'))

doc.preamble.append(header)
doc.change_document_style("header")

doc.append(NoEscape(r'\maketitle'))

doc.preamble.append(Command('captionsetup', 'belowskip=6pt,aboveskip=2pt'))
# 正文
# doc.append(Command('input', 'sec1.tex'))

# 插入tex原文

with doc.create(Chapter('some')) as chap:

    chap.append(Section('adsfas'))

    with open('plaintext.tex') as infile:
        for line in infile:
            chap.append(NoEscape(line))

    with chap.create(Section('插图')):

        # 插图
        with chap.create(Figure(position='htpb')) as logo:
            logo_file = os.path.join(os.path.dirname(__file__), 'logo.png')
            logo.add_image(logo_file, width=NoEscape(r'0.2\textwidth'))
            logo.add_caption('logo of hit')
            logo.append(Label('fig:hitlogo'))

        chap.extend(['如图', Ref('fig:hitlogo'), '所示'])

with doc.create(Chapter('表格')) as chap:

    with chap.create(Section('Tabu表格')) as sect:

        # 插入tabu表格
        with sect.create(Tabu("X[l] X[r]")) as first_page_table:
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

    with chap.create(Section('LongTabu表格')) as sect:

        with sect.create(
                LongTabu(" X[l]  X[l]  X[r]  X[r]  X[r] "
                         # row_height=1.5
                         )) as data_table:

            data_table.append(Command('caption', '数据'))
            data_table.append(Command('label', 'Tab:1'))
            data_table.append(NoEscape(r'\\'))

            data_table.append(Command('toprule'))
            data_table.add_row([
                "date", "description", "debits($)", "credits($)", "balance($)"
            ],
                               mapper=bold,
                               color="lightgray")
            data_table.add_hline()

            data_table.append(Command(r'endfirsthead'))

            data_table.append(Command('caption', '数据(续表)'))
            data_table.append(NoEscape(r'\\'))
            data_table.append(Command('toprule'))

            data_table.add_row(
                [
                    "date", "description", "debits($)", "credits($)",
                    "balance($)"
                ],
                mapper=bold,
                # color="lightgray"
            )
            data_table.add_hline()

            data_table.end_table_header()

            # data_table.add_hline()
            # data_table.add_bottomline()

            data_table.append(Command('bottomrule'))
            data_table.add_row((MultiColumn(5, align='r', data='续表见下页'), ))
            # data_table.add_hline()
            data_table.end_table_footer()

            # data_table.add_hline()
            # data_table.add_row((MultiColumn(3, align='r',
            #                     data='Not Continued on Next Page'),))
            # data_table.add_hline()

            data_table.append(Command('bottomrule'))
            data_table.end_table_last_footer()

            row = ["2016-JUN-01", "Test", "$100", "$1000", "-$900"]
            for i in range(50):
                if (i % 2) == 0:
                    data_table.add_row(row, color="lightgray")
                else:
                    data_table.add_row(row)

                # data_table.add_hline()

            data_table.append(Command('bottomrule'))

    # # 仅生成tex文档
    # # doc.generate_tex()

# 生成pdf文件
doc.generate_pdf(compiler='latexmk',
                 compiler_args=['-xelatex'],
                 clean_tex=False)
# doc.generate_pdf(clean_tex=False)
