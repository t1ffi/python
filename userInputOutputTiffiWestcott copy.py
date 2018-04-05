#Tiffi Westcott
#This program calculates a superstitious number using user input/output.

# Requests three things from user: first, last names and positive integer greater than 10.
firstName = input('Please type out your first name below: ')
lastName = input('Please type out your last name below: ')
x = input('Please type out a positive integer greater than 10: ')

#Uses concatenation to print user's first & last names with space between each.
print ('Hello', firstName, lastName)

#Uses modular division by 9 to divide posInteger to produce a number between 0 and 8. Then it adds one to that number.
modularInteger = (int(x))%9 + 1

#Prints preface and final number. 
print('This number may figure significantly in your life in the near future:', modularInteger)
