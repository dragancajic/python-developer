#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 13:29:11 2023

@author: Драган Ћајић

~ 02-01 if Statement ~
----------------------
"""
friend = "Momcilo"

user_name = input("Enter your name: ")

# if boolean:
#   execute some code
#   (body of if statement)
if user_name == friend:
    print("Hello, friend!")
    print("This runs too.")

print("This runs anyway.")
    # print("Hello")  # ERROR!

if user_name != friend:
    print("Hello, stranger!")

# previous two(2) if statements can be written like:

# compound if statement / if statement with two branches
# if boolean:
#   body of if statement
# else:
#   some other code
if user_name == friend:
    print("Hello, friend!")
else:
    print("Hello, stranger!")
# --------------------------------------------- -
# Spyder IDE 5.4.3 -> useful keyboard shortcuts -
#    Ctrl+Shift+I  -> switch to IPython console -
#    Ctrl+Shift+E  -> switch to Editor window   -
# --------------------------------------------- -
# bool of 5 is True!
# bool of 0 is False!
print(bool(5))  # True
print(bool(0))  # False

if 5:  # It can just be a value. ;-)
    print("Runs.")

# This shows that the thing that you are put in if statement, DOES NOT have
# to be a Boolean comparison! It can JUST be A VALUE! <--- LOOK!

# bool of an empty string evaluates to False, i.e. if we don't type anything
# is FALSE.
name = input("Enter your name: ")
print(bool(name))  # 'Dragan' -> True, '' -> False

if name:
    print("We know your name.")

# So, this is one of these scenarios where putting the variable directly in
# the if statement can be useful.

# Example
# -------
friends = ["Rolf", "Bob", "Anne"]
family = ["Jen", "Charlie"]

user_name = input("Enter your name: ")

# if user_name == friends:
    
# `==` compares two things directly, and input function always gives us string
# but, friends is a list -- so, these two thing are never going to be equal to
# one another, just because they are not even the same type of data. So, use:

if user_name in friends:  # membership operator `in`
    print(f"Hello, {user_name}, my friend!")
#elif not bool(user_name):
# or
elif bool(user_name) == False:
    print("Please, stranger, enter your name!")
else:
    print(f"I don't know you, {user_name}")

# The `in` keyword checks for whether the `user_name` is a value contained
# withIN the friends collection.
