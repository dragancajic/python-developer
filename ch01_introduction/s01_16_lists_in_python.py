#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 07:17:06 2023

@author: Драган Ћајић

~ 01-16 Lists in Python ~
-------------------------
"""
# BEST PRACTICE:
# You want to keep data inside a list homogeneous, so of the same kind, because
# the data inside the list is no longer described by the variable name, e.g.:
friends: list = ["Nebojsa", 2, "Momcilo"]  # bad practice, highly discouraged!!

friends = ["Nebojsa", "Momcilo"]
print(len(friends))  # 2

# list inside list (list of friends and their ages)
friends = [["Nebojsa", 25], ["Momcilo", 30]]
print(friends[0][0])  # Nebojsa
print(friends[1][1])  # 30

# a long list of lists written a little bit prettier
friends = [
    ["Nebojsa", 25],
    ["Momcilo", 30],
    ["Vladimir", 35],
]

friends = ["Nebojsa", "Momcilo"]
friends.append("Vladimir")
print(friends)

friends.remove("Nebojsa")
print(friends)
