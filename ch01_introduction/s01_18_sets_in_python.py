#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 16:46:00 2023

@author: Драган Ћајић

~ 01-18 Sets in Python ~
------------------------
"""
# Sets are another collection, like Lists and Tuples, that contain multiple
# values inside of them.

# Sets don't hold order AND sets don't contain duplicate elements!
art_friends = {"Veljo", "Mico"}
science_friends = {"Momcilo", "Nebojsa"}

art_friends.add("Vladimir")
print(art_friends)

# duplicate element is NOT added to that set!
art_friends.add("Vladimir")
print(art_friends)

art_friends.remove("Veljo")
print(art_friends)

# One of the key USE CASES about sets is that it's very easy to compare one set
# to another, e.g.
# "What elements are in this set, that are not in this other set?",
# or
# "What elements are common between both sets?".

# For thing like that, the sets are useful.
