# 12:31 AM Saturday, March 25, 2023


# ~ 01-10 Python Strings ~
# ------------------------

age = 34

#print("You are " + age)  # TypeError: must be str, not int

# solution:
age = "34"
print("You are " + age)  # age is now variable of string type

# or
age = 34  # age is again numeric variable
print("You are " + str(age))  # age is now variable of string type
