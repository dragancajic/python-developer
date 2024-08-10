# 12:31 AM Saturday, March 25, 2023

"""
~ 01-10 Python Strings ~
------------------------
"""

AGE = 34

#print("You are " + age)  # TypeError: must be str, not int

# solution:
AGE = "34"
print("You are " + AGE)  # age is now variable of string type

# or
AGE = 34  # age is again numeric variable
print("You are " + str(AGE))  # age is now variable of string type
