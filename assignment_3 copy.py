# Try, Except, & Casting

# Tiffi Westcott


# Part 1

unit_price = 17

userInput = raw_input("Enter Widget Quantity: ")

valid = False

while not valid:
    try:
        quantity = int(userInput)
        valid = True
    except ValueError:
        print("Quantity entered is not integer! Try Again.")
        userInput = raw_input("Enter Widgets quantity: ")

total = quantity * unit_price
tax = total * 0.0575
print "\nTotal Amount is: ", total, "$"
print "Sales tax: ", tax, "$"
print "Net total is: ", (total + tax), "$" 
