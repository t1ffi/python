# Tiffi Westcott
# This program calculates the highway tax for Appaloosa County.

# Title of application
print "Highway Tax Calculator Application\n"

# Input
val = input("Enter a house value: ") 
taxes = 0.000314159

# Processing 
NewVal = (val * 91)/100 
HighwayTax = NewVal * taxes 

#Output
print "For a house estimated to be worth: ",val
print "Highway tax is: ",HighwayTax
