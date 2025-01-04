#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 21:52:13 2023

@author: Драган Ћајић

~ 01-17 Tuples in Python ~
--------------------------
"""

short_tuple = "Nebojsa", "Momcilo"  # can be done!
print(short_tuple)

# but

# better use brackets around tuple [elements]
a_bit_clearer = ("Nebojsa", "Momcilo")
print(a_bit_clearer)

print("-" * 34)

# Example 1:
not_tuple_in_list = ["Momcilo", "Nebojsa"]  # this is just LIST, not tuple in list!
print(not_tuple_in_list)
print(type("Momcilo"), type("Nebojsa"))
print(type(not_tuple_in_list))

print()  # just an empty line

# but

tuple_in_list = [("Momcilo", "Nebojsa")]  # this is the TUPLE inside of a list!
print(tuple_in_list)
print(type(("Momcilo", "Nebojsa")))
print(type(tuple_in_list))


print("-" * 34)

# Example 2:
NOT_A_TUPLE = "Momcilo"
print(NOT_A_TUPLE)
print(type(NOT_A_TUPLE))

print()  # just an empty line

# but THIS IS a Tuple <-- LOOK!
this_is_tuple = ("Momcilo",)  # be careful when using COMMA (,) -- IT DOES MATTER!
print(this_is_tuple)
print(type(this_is_tuple))

print("-" * 34)

friends = ("Momcilo", "Nebojsa")

# AttributeError: 'tuple' object has no attribute 'append'
# friends.append("Vladimir")  # ERROR!

# TypeError: can only concatenate tuple (not "str") to tuple
# friends = friends + "Vladimir",  # ERROR!

# but this is OK!
three_friends = friends + ("Vladimir",)
print(three_friends)
print(
    type(
        "Vladimir",
    )
)
print(type(("Vladimir",)))
print(type(three_friends))

# In Lists, you CAN add and remove elements, but in Tuples you CAN NOT!
# So, that's the KEY DIFFERENCE between LISTS and TUPLES!

# Tuples are useful for when you want to keep them unchanged. <-- LOOK!

# Most of the time, it's recommended to use Tuples OVER Lists, and only
# use Lists when you specifically want to allow modification or changes.
