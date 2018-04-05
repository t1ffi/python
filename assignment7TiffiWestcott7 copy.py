#Tiffi Westcott
#Assignment number 7 aims to create a calculator where one can see how many times
#on average they check their phones per hour in a day.

#This imports the time for a secret little timer at the bottom.
import time

#These are variables that set the number per hour and end usage to 0 to begin with.
numHour = 0
endUse = 0.0

#This is the while statement which asks for the number of tiemes per hour that the user checks their phones.
#It also includes a try and except section to ensure it is the correct type of input.
while True:
    print ('Please enter the amount of times that you check phone per hour %02d' % numHour,)
    num = input(': ')
    try:
        num = int(num)
    except ValueError:
        print ('Whoopsie! Something went wrong... try a valid integer.')
        continue
    endUse += num
    numHour += 1
    if numHour == 12:
        break
#The above statements initiate continue if the time is in between 0 and 12 and then breaks once it strikes midnight!
#Below is the equation that finds the answer for the user and prints.
numAverage = endUse / 12
print ('And... the average number of times you check phone in an hour is....')
#This is the timer I mentioned above!
time.sleep(5)
#This spits out the answer and thanks the user for tracking! 
print (numAverage, 'times per hour!')
print ('Thanks for tracking with us!')
