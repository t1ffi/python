#Tiffi Westcott
#This is a program to show the largest number and count the iterations until it reaches the number 500.

#Imports random and random integer. 
from random import randint

#Variables set to count iterations.
iteration = 0
largest = 0

#While loop created and set to true.
while True:
   iteration = iteration + 1
   
   #Variable determine randint
   number = randint(1,500)
   
   #This section determines the largest number and prints it.
   if number > largest:
       largest = number
       print ("The largest integer so far is ", largest)
       
   #Depending upon the break, this if statement prints the iteration total out.
   if largest == 500:
       print ("It took", iteration, "iterations to generate the number 500.")
       break
