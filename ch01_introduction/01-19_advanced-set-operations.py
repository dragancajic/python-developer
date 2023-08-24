#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 17:16:44 2023

@author: Драган Ћајић

~ 01-19 Advanced Set Operations ~
---------------------------------
"""
art_friends = {"Vladimir", "Veljo", "Mico"}
science_friends = {"Momcilo", "Nebojsa", "Veljo"}

# 1a.) A \ B = A \ (A intersect B)
# DIFFERENCE -> elements that are in one set, but NOT in the other
art_but_not_science = art_friends.difference(science_friends)
print(art_but_not_science)

science_but_not_art = science_friends.difference(art_friends)
print(science_but_not_art)

# vs.

# 1b.) A \\ B = (A \ B) U (B \ A) OR B \\ A = (B \ A) U (A \ B)
# -->  A ^ B = (A \ B) U (B \ A) OR B ^ A = (B \ A) U (A \ B) <-- more formal!
# SYMMETRIC DIFFERENCE -> elements that are NOT in BOTH sets
# symmetric difference (members that aren't in both sets) <-- LOOK!
# [union of both sets without members that are common for both sets]
not_in_both = art_friends.symmetric_difference(science_friends)
print(not_in_both)
# Sets don't hold order AND sets don't contain duplicate elements!
not_in_both = science_friends.symmetric_difference(art_friends)
print(not_in_both)

# 2) A intersect B
# INTERSECTION -> elements in both sets, e.g. set of one element {'Veljo'}
art_and_science = art_friends.intersection(science_friends)
print(art_and_science)

# 3) A U B
# UNION -> all elements without duplicates
all_friends = art_friends.union(science_friends)
print(all_friends)

# Example in practice: Lottery Game (intersection of winner set and user set!)

# Data Structures: Lists, Tuples, Sets
# Most of the time, you will be using Tuples and Lists.
# Sets are reserved when you want to use these (set) operations!
