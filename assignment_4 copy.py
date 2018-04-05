# Tiffi Westcott
# Assignment #4

#Ants & Grasshoppers - a Work Ethic Classifcation

print("Type 1 if you complete all your work before relaxing")
print("Type 2 if you relax before completing all your work")
print("Type 3 if you don't do alternate work and relaxing")

inp = input("Choose from above options: ")

try:
    number = int(inp)
    if number == 1:
        print("Rad! Your're an ant!")
    elif number == 2:
        print("Sick! You're a Grasshopper!")
    elif number == 3:
        print("Sweet! You're neither an ant nor a grasshopper")
    else:
        print("Dope! You should choose the valid option number")
except ValueError:
    print("Hunty, please enter a valid numerical choice.")
