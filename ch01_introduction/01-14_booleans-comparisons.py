#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 17 14:38:10 2023

@author: Драган Ћајић

~ 01-14 Booleans and Comparisons in Python ~
--------------------------------------------
"""

truthy = True
falsy = False

age = 20

is_over_age = age >= 18  # 20 >= 18 [is equal to] <=> True
is_under_age = age < 18  # 20 < 18  [is equal to] <=> False

is_twenty = age == 20    # 20 == 20 [is equal to] <=> True


# try to guess my magic number
my_number = 5
user_number = int(input("Enter a number: "))

matches = my_number == user_number

print(f"You got it right: {matches}.")
