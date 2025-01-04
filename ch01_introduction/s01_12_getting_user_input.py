#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 01:12:21 2023

@author: Драган Ћајић

~ 01-12 Getting User Input in Python ~
--------------------------------------
"""

MY_NAME = "Dragan"
your_name = input("Enter your name: ")

print(f"Hello {your_name}. My name is {MY_NAME}.")

# Anything that user types, even if it is the number 35, is a string! <-- LOOK!
# A string that contains the characters three('3') and five('5').

age = input("Enter your age: ")  # the whole line on the right of = sign is "3"!
age_num = int(age)
print(f"You have lived for {age * 12} months.")  # repeat string 12 times!
print(f"You have lived for {age_num * 12} months.")  # calculation - int √

AGE = int(input("Enter your age: "))
months = AGE * 12
print(f"You have lived for {months} months.")
