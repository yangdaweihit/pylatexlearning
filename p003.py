#!/usr/bin/env python3
"""
本例测试了PyLaTeX中页眉页脚功能，见headfoot.py：

1. PageStyle
2. Head
3. Foot

类关系：

ContainerCommand -> PageStyle |-> Head
                              |-> Foot

"""

# begin-doc-include
from pylatex import Document, PageStyle, Head, MiniPage, Foot, LargeText, \
    MediumText, LineBreak, simple_page_number
from pylatex.utils import bold


def generate_header():
    geometry_options = {"margin": "0.7in"}
    doc = Document(geometry_options=geometry_options)
    # Add document header
    header = PageStyle("header")
    # Create left header
    with header.create(Head("L")):
        header.append("Page date: ")
        header.append(LineBreak())
        header.append("R3")
    # Create center header
    with header.create(Head("C")):
        header.append("Company")
    # Create right header
    with header.create(Head("R")):
        header.append(simple_page_number())
    # Create left footer
    with header.create(Foot("L")):
        header.append("Left Footer")
    # Create center footer
    with header.create(Foot("C")):
        header.append("Center Footer")
    # Create right footer
    with header.create(Foot("R")):
        header.append("Right Footer")

    doc.preamble.append(header)
    doc.change_document_style("header")

    # Add Heading
    with doc.create(MiniPage(align='c')):
        doc.append(LargeText(bold("Title")))
        doc.append(LineBreak())
        doc.append(MediumText(bold("As at:")))

    doc.generate_pdf("p003", clean_tex=False)


generate_header()
