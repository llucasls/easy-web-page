#!/usr/bin/env python
import sys
from markdown import Markdown


try:
    input_file = sys.argv[1]
except IndexError:
    print("Error: input not found", file=sys.stderr)
    print("this script takes two arguments, and at least one is required",
          file=sys.stderr)
    sys.exit(1)


try:
    output_file= sys.argv[2]
except IndexError:
    output_file= "/dev/stdout"


markdown = Markdown(output_format="html", tab_length=4)
markdown.convertFile(input=input_file, output=output_file)


with open(output_file, mode="a") as file:
    print("", file=file)
