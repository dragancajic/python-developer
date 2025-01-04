#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 17 17:33:50 2023

@author: Драган Ћајић

~ 01-15 `and` and `or` in Python ~
----------------------------------
"""

# The Complete Python Course: https://go.tecla.do/cpc
# Lecture: The 'and' & 'or' keywords in Python
# E-book: https://complete-python.teclado.com/intro/lectures/and_or

# AGE = int(input("Enter your age: "))  # e.g. 25
AGE = 25
# RESULT = AGE > 18 and AGE < 65  # True and True
RESULT = 18 < AGE < 65

# The `or` keyword just returns the second value if the first one evaluates to `False`!
RESULT = AGE < 18 or AGE < 65  # False or (True)
print(RESULT)  # True

print("=" * 8)

# Truthy and Falsy Values
bool(0)  # False
bool(13)  # True

print(bool(0))
print(bool(13))

bool("")  # False, empty string!
bool("Hello")  # True

print(bool(""))
print(bool("Hello"))

bool([])  # False, empty list!
bool([1, 3, 5])  # True

print(bool([]))
print(bool([1, 3, 5]))

print("=" * 8)

DEFAULT_AGE = 30
AGE = 0

USER_AGE = AGE or DEFAULT_AGE
print(USER_AGE)

print("=" * 8)

DEFAULT_GREETING = "there"
name = input("Enter your name: (optional) ")

user_name = name or DEFAULT_GREETING
print(f"Hello, {user_name}!")

print("=" * 8)

# If the value on the left of the `and` operator is truthy, we get the value
# on the right of the operator, e.g. number `18`!!! <-- LOOK!
X = True
CMP = X and 18
print(CMP)  # 18

AGE = 16
SIDE_JOB = True

# Simplify chained comparison between the operands | Pylint
# (R1716:chained-comparison)
# https://pylint.readthedocs.io/en/latest/user_guide/messages/refactor/chained-comparison.html
print(AGE > 18 and AGE < 65 or SIDE_JOB)  # True

# so, after simplifying, it would be like this:
print(18 < AGE < 65 or SIDE_JOB)  # True

# The COMPARISONS evaluate first, and then `and` and `or` evaluate left to right.
# print((AGE > 18) and (AGE < 65) or SIDE_JOB)  # True
# print((18 < AGE < 65) or SIDE_JOB)  # True
