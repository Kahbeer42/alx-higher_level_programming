kip to content
ephayeabe
/
alx-higher_level_programming
Public
Code
Issues
Pull requests
Actions
Projects
Security
Insights
alx-higher_level_programming/0x0B-python-input_output/1-write_file.py
@ephayeabe
ephayeabe create 1-write_file.py
 1 contributor
10 lines (8 sloc)  257 Bytes
#!/usr/bin/python3
"""
Contains the function "wrtie_file"
"""


def write_file(filename="", text=""):
    """returns the number of chars written to "filename" from "text" """
    with open(filename, 'w', encoding='utf=8') as f:
        return f.write(text)
