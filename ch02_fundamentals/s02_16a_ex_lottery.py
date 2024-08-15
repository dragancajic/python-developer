#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 17:36:30 2024

@author: dragancajic

~ 02-16a Exercise: An Improved Lottery! (Python 3.10) ~
------------------------------------------------------
"""
import config

# This line loads a set of 6 random numbers from the config file
lottery_numbers = config.lottery_numbers

# Here are your players; find out who has the most numbers matching lottery_numbers!
players = [
    {"name": "Rolf", "numbers": {1, 3, 5, 7, 9, 11}},
    {"name": "Charlie", "numbers": {2, 7, 9, 21, 10, 5}},
    {"name": "Anna", "numbers": {13, 14, 15, 16, 17, 18}},
    {"name": "Jen", "numbers": {19, 20, 12, 7, 3, 5}},
]

# Then, print out a line such as "Jen won 1000.".
# The winnings are calculated with the formula:
# 100 ** len(numbers_matched)
print(lottery_numbers)
# print(type(lottery_numbers))  # <class 'set'>

player_scored = []

for i, player in enumerate(players):
    numbers_matched = player['numbers'].intersection(lottery_numbers)
    player_scored.append((player['name'], len(numbers_matched)))


    if len(numbers_matched) != 0:
        print('Name:', player['name'], 'No.', i)
        print('Numbers match:', numbers_matched)
        print('No. of matching:', len(numbers_matched), '\n')

print(player_scored)  # list of tuples

MAX_NO = 0
for i, player in enumerate(player_scored):
    # print(i, player[0], player[1])
    if player[1] > MAX_NO:
        name, max_no = player[0], player[1]

print(f"{name} won {100**MAX_NO}.")
