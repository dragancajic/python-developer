#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 03:49:37 2023

@author: Драган Ћајић

~ Exercise: Communicating with Users (Python 3.10) ~
----------------------------------------------------
"""

# First, ask the user for their name. Then, print out the greeting "Hello, NAME"
# Remember the uppercase H, the comma, and the space between words!

# Secondly, ask the user for their age and convert it into a number.
# Then, print out how many months that equals to (you'll have to multiply the age by 12).
name = input("What's your name: ")
print(f"Hello, {name}")

age = int(input("What's your age: "))
months = age * 12
print(f"Your age in months is {months}")
