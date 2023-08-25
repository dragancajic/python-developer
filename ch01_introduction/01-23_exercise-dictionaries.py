#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 09:33:22 2023

@author: Драган Ћајић

~ Exercise: Dictionaries (Python 3.10) ~
----------------------------------------
"""
# Lottery numbers
lottery_numbers = {13, 21, 22, 5, 8}


"""
A player looks like this:

{
    'name': 'PLAYER_NAME',
    'numbers': {1, 2, 3, 4, 5}
}

Define a list with two players (you can come up with their names and numbers).
"""

players = [
    {"name": "Momcilo", "numbers": {1, 2, 3, 4, 5}},
    {"name": "Nebojsa", "numbers": {3, 22, 10, 6, 5}}
]

"""
For each of the two players, print out a string like this:
    "Player PLAYER_NAME got 3 numbers right.".
Of course, replace PLAYER_NAME by their name, and the 3 by the amount of numbers
they matched with lottery_numbers.
You'll have to access each player's name and numbers, and calculate the intersection
of their numbers with lottery_numbers. Then construct a string and print it out.

Remember: the string must contain the player's name and the amount of numbers they got right!
"""
player1_name = players[0]["name"]
player1_numbers = players[0]["numbers"]
player1_match_nums = lottery_numbers.intersection(player1_numbers)
player1_match_count = len(player1_match_nums)

player2_name = players[1]["name"]
player2_numbers = players[1]["numbers"]
player2_match_nums = lottery_numbers.intersection(player2_numbers)
player2_match_count = len(player2_match_nums)

print(f"Player {player1_name} got {player1_match_count} right.")
print(f"Player {player2_name} got {player2_match_count} right.")
