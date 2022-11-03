# Easy Web Page

The purpose of this repository is to create a template for easily building new
web pages. It should create a complete web page from a markdown file.

## Usage:

```
./generate.py [input_file] [output_file]
```

This script converts markdown into html. The input and output files are
optional.

If no argument is given, it will ask the user for the input file name,
and write the html code to `stdout`.

If one file name is given, it will read the content as markdown and print the
converted html to `stdout`.

If both file names are provided, the script will silently write to the output
file.
