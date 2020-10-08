#!/usr/bin/python
"""
This example shows subfigure functionality.

..  :copyright: (c) 2014 by Jelte Fennema.
    :license: MIT, see License for more details.

本例测试了PyLaTeX如下功能：

- SubFigure

"""

# begin-doc-include
from pylatex import Document, Section, Figure, SubFigure, \
    NoEscape, Command, Package
import os

if __name__ == '__main__':
    doc = Document(default_filepath='p004')

    doc.packages.append(Package('ctex', options=r'UTF8'))

    image_filename = os.path.join(os.path.dirname(__file__), 'logo.png')

    with doc.create(Section('插入子图')):
        with doc.create(Figure(position='h!')) as kittens:
            with doc.create(SubFigure(
                    position='b',
                    width=NoEscape(r'0.5\linewidth'))) as left_kitten:

                left_kitten.append(Command('centering'))
                left_kitten.add_image(image_filename,
                                      width=NoEscape(r'0.6\linewidth'))
                left_kitten.add_caption('左边一个')
            with doc.create(SubFigure(
                    position='b',
                    width=NoEscape(r'0.5\linewidth'))) as right_kitten:

                right_kitten.append(Command('centering'))
                right_kitten.add_image(image_filename,
                                       width=NoEscape(r'0.6\linewidth'))
                right_kitten.add_caption('右边一个')
            kittens.add_caption("两个校徽")

    doc.generate_pdf(compiler='latexmk',
                     compiler_args=['-xelatex'],
                     clean_tex=False)
