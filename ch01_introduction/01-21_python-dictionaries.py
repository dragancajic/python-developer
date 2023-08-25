#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 23:04:00 2023

@author: Драган Ћајић

~ 01-21 Python Dictionaries ~
-----------------------------
"""
# dictionary -> "KEY": "VALUE" -> know "key", get "value" back
friend_ages = {"Rolf": 24, "Adam": 30, "Anne": 27}

print(friend_ages["Rolf"])

# add new element, by adding key: value pair, like this
friend_ages["Bob"] = 20

# you can't do this -> key: value in the same place for accessing purpose!
# TypeError: unhashable type: 'slice'
#friend_ages["Bob": 20]  # ERROR!
# nor this
#friend_ages["Bob"]: 20  # no error, but wrong doing!

# change value of/for existing key in the dictionary
friend_ages["Rolf"] = 25

print(friend_ages)

# Dictionaries DO KEEP THE ORDER in which you added keys to them, as of
# Python 3.7. Sets don't keep the order of their elements, as you know!

# But, like in Sets, you CAN NOT HAVE DUPLICATE KEYS in dictionary!

# So, you can not have duplicate keys, but the order is kept. <-- LOOK!

# USE CASE: Program that stores information about your friends
# ---------
# For multiple friends and multiple pieces of information about them,
# the best thing to do is to use a List or a Tuple of Dictonaries:

# Tuple with three(3) elements -- Dictionaries;
# This is very typical Use Case of Dictionaries, which is to store information
# in the way that will be EASILY RETRIEVABLE and in the way that is SIMILAR to
# other Dictionaries that are related!
# ~ bad example:
'''
friends = (
    {"Rolf Smith": 24},  # you can not access the name of each friend!
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27}
)
'''
# You would need to know the name of each friend, before you can access the value!
# So, by doing something like this:
friends = (
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27}
)
# what that allows us to do is to say
print(friends[0]["name"])
print(friends[1]["name"])
print(friends[2]["name"])
# accessing the `name` property of the dictionary

# or like this
# friend = friends[0]
# print(friend["name"])

# This can be particularly useful when you have a lot of friends, or a lot of
# data in your List and in your Tuple and you want the data to be homogeneous,
# so that you can always ACCESS THE SAME KEY for each piece of data.

# dict() function
friends = [("Rolf", 24), ("Adam", 30), ("Anne", 27)]  # list of tuples

friend_ages = dict(friends)
print(friend_ages)
# which is used to turn data into a dictionary

# So, this can be useful, because there are many different parts of Python
# that will give you data in this format -----> LIST OF TUPLES
# [("Rolf", 24), ("Adam", 30), ("Anne", 27)]  # list of tuples
# instead of a dictionary, and turn them into a dictionary like this can be
# very handy! <----- LOOK!
