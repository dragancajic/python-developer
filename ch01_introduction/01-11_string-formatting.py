#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 11:25:52 2023

@author: Драган Ћајић

~ 01-11 Python String Formatting ~
----------------------------------
"""

age = 34

age_as_str = str(age)

print("You are " + age_as_str)

# f-strings from Python >= 3.6
print(f"You are {age}")


name = "Драган"
greeting = f"How are you, {name}?"
print(greeting)

# limitation with f-strings
name = "Bojan"
print(name)      # output: Bojan
print(greeting)  # name in f-string doesn't change after reassignment!

# That is why Python has another way of formatting strings which does allow
# for the changing of variables:

name = "Luka"  # value for placeholder of the final_greeting string

# final_greeting is the template for a greeting
final_greeting = "How are you, {}?"  # placeholder {} is replaced by the value
luka_greeting = final_greeting.format(name)
print(luka_greeting)

bojan_greeting = final_greeting.format("Bojan")  # new value for placeholder!
print(bojan_greeting)

# another way of using template string
name = "Nada"
final_greeting = "How are you, {name}?"  # this is not an f-string! LOOK!
nada_greeting = final_greeting.format(name = "N a d a")  # <-- L O O K !

print(final_greeting)
print(nada_greeting)

# confusing thig is THIS -> name = name (two[2] completely different variables!)
nada_greeting = final_greeting.format(name = name)  # DIFFERENT variables!!!

print(final_greeting)
print(nada_greeting)

mother_name = "N_a_d_a"
nada_greeting = final_greeting.format(name = mother_name)

print(final_greeting)
print(nada_greeting)

# Usually, you will be using f-strings in Python just because they are shorter,
# they are more readable, you don't have to type like .format and then brackets
# and passing things there. So, f-strings are the weapon of choice.
# But, somethimes when you want to reuse a template using format, comes in handy.
