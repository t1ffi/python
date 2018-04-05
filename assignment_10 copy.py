# Tiffi Westcott

# Lists!

import random
numlist1 = []
numlist2 = []

for i in range(0,100):
    rando = random.randint(1,1000000);
    numlist1.append(rando)

for newbie in numlist1:
    if (newbie%13 == 0 and (newbie/13)%2 == 0): 
        numlist2.append(newbie)

print "Here is the brand new list:", "\n", numlist2
print "Number of numbers in my new list is", len(numlist2)

if len(numlist2) != 0:
    print "The largest in my new list is", max(numlist2)
    print "The smallest in new list is", min(numlist2)
