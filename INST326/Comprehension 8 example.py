"""Comprehension check 8
"""

import re

with open("speech.txt","r") as file:
    fileData = f.read()
    found = re.findall(r"for", fileData)
    print("Number of for", len(found))