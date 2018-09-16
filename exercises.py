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

Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.

Extras:

Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it 
and print out this new list.
Write this in one line of Python.
Ask the user for a number and return a list that contains only elements from the original list a that are smaller than 
that number given by the user.

'''

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

b = [i for i in a if i <=5 ]
# print(b)

c = input("Type in a number:\n")
c = int(c)

d = [i for i in a if i < c]
print(d)

'''

Exercise 4:

Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
(If you don’t know what a divisor is, it is a number that divides evenly into another number. 
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

'''

# ask user for input
a = input("Type in a number: \n")
a = int(a)

# generate a list based on the user input
# the a + 1 generates a higher number than a so we're sure we'll find the user's number in the list
list_range = list(range(1, a +1))

# create an empty list to append the results
divisor_list = []

# divide a to all the number in the list and if i in the list is a divisor of a, then append it to the newly created list
for i in list_range:
    if a % i == 0:
        divisor_list.append(i)

# output the result
print(divisor_list)

'''

Exercise 5:



'''
