#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 11:22:05 2024

@author: dragancajic

~ 10-13 Exercise: Secure File Names using RegEx (Python 3.10) ~
---------------------------------------------------------------
"""

import re

# Our definition of a secure filename is:
# - The filename must start with an English letters or a number (a-zA-Z0-9).
# - The filename can **only** contain English letters, numbers and symbols
#   among these four: `-_()`.
# - The filename must end with a proper file extension among `.jpg`, `.jpeg`,
#   `.png` and `.gif`.


def is_filename_safe(filename):
    """Check if filename is safe"""
    # you only need to change the regular expression (regex) below
    # regex = r'^[a-zA-Z0-9-_()]+\.(jpg|jpeg|png|gif)$'
    regex = r'^[a-zA-Z0-9][a-zA-Z0-9_()-]*(\.jpg|\.jpeg|\.png|\.gif)$'
    return re.match(regex, filename) is not None


print(is_filename_safe('picture'))          # False
print(is_filename_safe('picture.png'))      # True
print(is_filename_safe('picture#.png'))     # False
print(is_filename_safe('picture-1.png'))    # True
print(is_filename_safe('_aer3244c12.jpg'))  # True <-- WA? | False √
print(is_filename_safe('32c12.jpg'))        # True

# test case (WA)
# is_filename_safe("(aer3244c12.jpg") should return False
# but in your code it returned True.
