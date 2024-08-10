#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 11:25:52 2023

@author: Драган Ћајић

~ 01-11 Python String Formatting ~
----------------------------------
"""

AGE = 34

AGE_AS_STR = str(AGE)

print("You are " + AGE_AS_STR)

# f-strings from Python >= 3.6
print(f"You are {AGE}")


NAME = "Драган"
greeting = f"How are you, {NAME}?"
print(greeting)

# limitation with f-strings <-- LOOK! :eyes:
NAME = "Bojan"
print(NAME)      # output: Bojan
print(greeting)  # `NAME` in f-string doesn't change after reassignment!

# That is why Python has another way of formatting strings which does
# allow for the changing of variables:

NAME = "Luka"  # value for placeholder of the `FINAL_GREETING` string

# `FINAL_GREETING` is the template for a `greeting`
FINAL_GREETING = "How are you, {}?"  # placeholder {} is replaced by the value
LUKA_GREETING = FINAL_GREETING.format(NAME)
print(LUKA_GREETING)

BOJAN_GREETING = FINAL_GREETING.format("Bojan")  # new value for placeholder!
print(BOJAN_GREETING)

# another way of using template string
NAME = "Nada"
FINAL_GREETING = "How are you, {NAME}?"  # this is not an f-string! LOOK!
NADA_GREETING = FINAL_GREETING.format(NAME = "N a d a")  # <-- L O O K !

print(FINAL_GREETING)
print(NADA_GREETING)

# confusing thing is THIS -> name = name (two[2] completely different variables!)
NADA_GREETING = FINAL_GREETING.format(NAME = NAME)  # DIFFERENT variables!!!

print(FINAL_GREETING)
print(NADA_GREETING)

MOTHER_NAME = "N_a_d_a"
NADA_GREETING = FINAL_GREETING.format(NAME = MOTHER_NAME)

print(FINAL_GREETING)
print(NADA_GREETING)

# Usually, you will be using f-strings in Python just because they are shorter,
# they are more readable, you don't have to type like .format and then brackets
# and passing things there. So, f-strings are the weapon of choice.
# But, somethimes when you want to reuse a template using format, comes in handy.
