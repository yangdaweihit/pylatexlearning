#!/usr/bin/python
"""
This example shows the functionality of the MiniPage element.

It creates a sample page filled with labels using the MiniPage element.

..  :copyright: (c) 2014 by Jelte Fennema.
    :license: MIT, see License for more details.

本例测试了PyLaTeX如下功能：

- Tabularx
- MiniPage

"""

# begin-doc-include
from pylatex import Document, Section, Figure, Command, \
    Package, Table, Tabu, Label, MiniPage
from pylatex.utils import bold
import os

if __name__ == '__main__':
    doc = Document(default_filepath='p005')

    doc.packages.append(Package('ctex', options=r'UTF8'))

    image_filename = os.path.join(os.path.dirname(__file__), 'logo.png')

    with doc.create(Section('表格里插图')):

        with doc.create(Table(position='htpb')) as table:
            table.append(Command('centering'))
            table.append(Command('caption', '外观检测'))
            table.append(Command('label', 'tbl:inspect'))

            with table.create(
                    Tabu("X[l] X[3,l]", booktabs=True,
                         to='90mm')) as tabu:

                tabu.add_topline()
                tabu.add_row(["date", "description"], mapper=bold)
                tabu.add_hline()
                tabu.add_row(["2020-10-05", "meeting"])
                tabu.add_bottomline()

    doc.generate_pdf(compiler='latexmk',
                     compiler_args=['-xelatex'],
                     clean_tex=False)
