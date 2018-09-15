''' 

Exercise 1:
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year 
that they will turn 100 years old.

Extras:

Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. 
(Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)

'''

 # import datetime so that we'll know the current year
from datetime import datetime

# this variable provides us the current year
year = datetime.now().year

# ask the user to type in his name and his age
name = input("Type in your name:\n")
age = input("How old are you?\n")
age = int(age)

# make the difference between 100 years and user's age, then make the sum to find out when the user will be 100 years old
agediff = (100 - age)
age100 = (year + agediff)

# display the results
print("Your name is ", name, "and you are", age, "years old.")
print("You'll be 100 years old in", age100)

'''

Exercise 2:

