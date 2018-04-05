import sys
import random
import time

#This assignment makes a magic 8 ball - the hard way! :)

#Below I commented out probably the most efficient way to create one. 

# responses = ["Meh probs not", "Heck nah, bro" "U kidding me? No way, henny", "What? Did you say something?", "I'm busy atm, come back later tho", "Too much haze in the air...", "Um, YAS, Queen!", "Duh, of course!", "Heck yeah, playa!", "Ayo, BINGO!"]

# userInput = input('Please input a yes or no question: ')

# print(random.choice(responses))

#Asks user to put in a yes or no question
userInput = input('Please input a yes or no question: ')

#Delays program for 3 seconds and requires user to activate like a real 8-ball.
input("Please press enter to continue")
time.sleep(3)

#Random function that returns random int between 1 and 10
for x in range (1):
    x = random.randint(1,10)

#If elif else statements 
if x ==1:
    print ("Meh probs not")
elif x ==2:
    print ("Heck nah, bro")
elif x ==3:
    print ("U kidding me? No way, henny")
elif x ==4:
    print ("What? Did you say something?")
elif x ==5:
    print ("I'm busy atm, come back later tho")
elif x ==6:
    print ("Too much haze in the air...")
elif x ==7:
    print ("Um, YAS, Queen!")
elif x ==8:
    print ("Duh, of course!")
elif x ==9:
    print ("Heck yeah, playa!")
elif x ==10:
    print ("Ayo, BINGO!")
else:
    print("EPIC GENERATOR FAIL! Try again.")
