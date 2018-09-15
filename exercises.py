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

Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. 
Hint: how does an even / odd number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

'''

num = input("Enter a number:\n")
num = int(num)

check = num % 4
check2 = num % 2

if check == 0:
    print("The number", num, "is even and a multiple of 4.")
elif check2 == 0:
    print("The number", num, "is even and divides by 2, not by 4.")
else:
    print("The number", num, "is odd.")
 
'''

Exercise 3:
