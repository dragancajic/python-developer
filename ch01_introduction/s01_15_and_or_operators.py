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

#age = int(input("Enter your age: "))  # e.g. 25
age = 25
result = age > 18 and age < 65  # True and True

# The `or` keyword just returns the second value if the first one evaluates to `False`!
result = age < 18 or age < 65  # False or (True)
print(result)

print("=" * 8)

# Truthy and Falsy Values
bool(0)   # False
bool(13)  # True

print(bool(0))
print(bool(13))

bool("")       # False, empty string!
bool("Hello")  # True

print(bool(""))
print(bool("Hello"))

bool([])         # False, empty list!
bool([1, 3, 5])  # True

print(bool([]))
print(bool([1, 3, 5]))

print("=" * 8)

default_age = 30
age = 0

user_age = age or default_age
print(user_age)

print("=" * 8)

default_greeting = "there"
name = input("Enter your name: (optional) ")

user_name = name or default_greeting
print(f"Hello, {user_name}!")

print("=" * 8)

# If the value on the left of the `and` operator is truthy, we get the value
# on the right of the operator, e.g. number `18`!!! <-- LOOK!
x = True
cmp = x and 18
print(cmp)  # 18

age = 16
side_job = True
print(age > 18 and age < 65 or side_job)  # True
# The conditionals evaluate first, and then `and` and `or` evaluate left to right.
