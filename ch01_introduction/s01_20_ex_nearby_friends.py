#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 18:42:47 2023

@author: Драган Ћајић

~ Exercise: Nearby Friends (Python 3.10) ~
------------------------------------------
"""
nearby_people = {'Rolf', 'Jen', 'Anna'}
user_friends = set()  # This is an empty set, like {}

# Ask the user for the name of a friend
name_of_friend = input("What's your friend's name: ")

# Add the name to the empty set
user_friends.add(name_of_friend)

# Print out the intersection between both sets.
# This gives us a set with those friends that are nearby.
nearby_friend = nearby_people.intersection(user_friends)

if nearby_friend:
    print(f">>> {name_of_friend} is your nearby friend! ;-)")
else:
    print(f"You don't have nearby friend with {name_of_friend}!")
