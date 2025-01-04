#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 17 14:38:10 2023

@author: Драган Ћајић

~ 01-14 Booleans and Comparisons in Python ~
--------------------------------------------
"""

TRUTHY = True
FALSY = False

AGE = 20

IS_OVER_AGE = AGE >= 18  # 20 >= 18 [is equal to] <=> True
IS_UNDER_AGE = AGE < 18  # 20 < 18  [is equal to] <=> False

IS_TWENTY = AGE == 20  # 20 == 20 [is equal to] <=> True


# try to guess my magic number
MY_NUMBER = 5
user_number = int(input("Enter a number: "))

matches = MY_NUMBER == user_number

print(f"You got it right: {matches}.")
