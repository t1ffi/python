#Tiffi Westcott
#Exam 1: asks for two positive integers and decides which are bigger, resulting in modular division that is spit out to the user. 

#Requests two positive integers from user.
firstInput = input("Enter your first positive integer: ")

#Try - except loops verify inputs are integers.
try:
    intInput1 = int(firstInput)
    if intInput1 < 0:
        print ("That is not a positive integer.")
except ValueError:
    print ("The input is not valid.")

#Requests two positive integers from user.
secondInput = input("Enter your second positive integer: ")

#Try - except loops verify inputs are integers.
try:
    intInput2 = int(secondInput)
    if intInput2 < 0:
        print ("That is not a positive integer.")
except ValueError:
    print ("That's not valid input.")

#Puts division statements into variables for ease of use.
division1 = intInput1%intInput2
division2 = intInput2%intInput1

#If - elif - else determines which of the numbers are smaller and larger, then prints result statements.
if intInput1 > intInput2:
    print ("The number that is larger is: ", repr(intInput1), "and the number that is smaller is", repr(intInput2),".")
    print ("The division result is... ", division1,".")
elif intInput2 > intInput1:
    print ("The number that is larger is: ", repr(intInput2), "and the number that is smaller is", repr(intInput1),".")
    print ("The division result is... ", division2,".")
else:
    print ("The numbers are both equal: ", intInput1,".")
