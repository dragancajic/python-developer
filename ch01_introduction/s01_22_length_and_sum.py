#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 08:35:44 2023

@author: Драган Ћајић

~ 01-22 Length and Sum [of List] ~
----------------------------------
"""
grades = [80, 75, 90, 100]

# calculate an average of a list [elements] using sum() and len() functions
# calculate the average of [these] grades
total = sum(grades)   # sum up the elements of the list, or tuple, or set
length = len(grades)  # len(collection) gives you the length of collection

average = total / length
print(average)

# Quick Question: Which of these Data Structures is less ideal for grades?
grades = [80, 75, 90, 100]  # a list of grades
grades = (80, 75, 90, 100)  # a tuple of grades
grades = {80, 75, 90, 100}  # a set of grades √

# The tuple of grades: you can not add new grades over time!
# But, the set of grades is the worst choice (no duplicates, e.g. 100, 100)!

# So, the SET is the worst of these collections for the use case -- storing
# student grades; the TUPLE might be a bad idea depending on what you want to
# do in your programme / program (Brit, Cdn / US), and the LIST is the safest
# of them all.

# List allows you total flexibility while giving you all the power you need!

# REMEMBER:
# If you do not have to add more things to your collection -- use a tuple!
# Otherwise -- use the list.
# Only use sets for when you want to compare sets together!!! <----- LOOK!
