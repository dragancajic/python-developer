#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 04:28:07 2023

@author: Драган Ћајић

~ 01-24 Joining a List ~
------------------------
"""
# join() allows you to print out your lists a bit better
friends = ["Nebojsa", "Momcilo", "Vladimir"]
print(type(friends))

print(f"My friends are {friends}.")

# join elements of a list by specified separator (`,` | ` & ` | ...) into one
# string [<class 'str'>] for better printing of your list <------------ LOOK!
comma_separated = ", ".join(friends)
print(type(comma_separated))

# each value of the list is taken and we've made one long string:
# "Nebojsa, Momcilo, Vladimir"
print(f"My friends are {comma_separated}.")

comma_separated = " & ".join(friends)
# "Nebojsa & Momcilo & Vladimir"
print(f"My friends are {comma_separated}.")
