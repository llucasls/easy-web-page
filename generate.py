#!/usr/bin/env python
import sys
from markdown import Markdown
from subprocess import check_output


try:
    input_file = sys.argv[1]
except IndexError:
    input_file = input("please state the name of the input file: ")
    print("\n")


try:
    output_file= sys.argv[2]
except IndexError:
    output_file= "/dev/stdout"


markdown = Markdown(output_format="html", tab_length=4)
markdown.convertFile(input=input_file, output=output_file)


with open(output_file, mode="a") as file:
    print("", file=file)
