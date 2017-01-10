#! /usr/bin/env python
"""converts all .md files to pdf using pandoc and latex
sends them to directory pdf"""
import subprocess
import os

for filename in os.listdir():
    if ".md" in filename:
        print(filename)
        subprocess.call(['pandoc', filename, "-o", "pdf/"+filename.replace(".md",".pdf")])
