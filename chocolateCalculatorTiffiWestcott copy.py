#Tiffi Westcott
#This program calculates the price of chocolates.

darkChoco = 1.25
milkChoco = 0.95
whiteChoco = 1.30
#Assign the price of each variety of chocolate to a variable

darkChocoAmnt = input("Enter amount of dark chocolate you would like: ")
darkChocoAmnt = int(darkChocoAmnt )
milkChocoAmnt = input("Enter amount of milk chocolate you would like: ")
milkChocoAmnt = int(milkChocoAmnt)
whiteChocoAmnt = input("Enter amount of white chocolate you would like: ")
whiteChocoAmnt = int(whiteChocoAmnt)
#User enters their wish to purchase 3 dark, 2 milk, and 1 white chocolate creams.
#The second line beneath it lets the compilier know that the code is an integer.

totalNoTax = darkChoco * darkChocoAmnt + milkChoco * milkChocoAmnt + whiteChoco * whiteChocoAmnt
print("The total price without tax is: ", totalNoTax, "dollars.")
#Calculates the cost of the chocolates.

salesTax = .0795
#Sales tax as a variable 

totalTax = totalNoTax * salesTax
print("Total tax amount comes to: ", totalTax ,"cents.")
#Calculates sales tax.

totalWithTax = totalNoTax + totalTax
print("Your final total with tax is:", totalWithTax , "dollars.")
#Calculates the total cost of chocolates by adding the sales tax.
#All output that prints is labeled accordingly. 


