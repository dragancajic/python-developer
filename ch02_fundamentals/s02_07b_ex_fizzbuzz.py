#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 18:49:29 2024

@author: dragancajic

~ 02-07b  Exercise: FizzBuzz (Python 3.10) ~
--------------------------------------------
"""

# Print out numbers from 1 to 100 (including 100).
# But, instead of printing multiples of 3, print "Fizz".
# Instead of printing multiples of 5, print "Buzz".
# Instead of printing multiples of both 3 and 5, print "FizzBuzz".

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
