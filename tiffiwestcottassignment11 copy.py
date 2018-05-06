'''Tiffi Westcott
Validates a given IP address in this program.''' 


'''The variable ip is given the user input.'''

ip = input("Hello, user! Please input a valid IP address. Pro tip: a valid IP address is formatted like so: _._._._ The underscore would be replaced by an integer ranging from 0 to 255: ")


'''The variable i initializes the counter'''

i = 0


'''Print is spitting out the first variable.'''

print ("Your IP entered is: " + ip)


try:
    '''Variable token tokenizes the input given.'''
    token = ip.split(".")

    '''The length of the given IP address is now validated.'''
    if len(token) != 4:
        print ("Looks like this IP address is invalid. Are there numbers missing?")
    else:
        for i in range (0, len(token)):

            '''The X variable stores the token.'''
            x = int(token[i])

            '''This is checking the token, it validates each portion that was
            tokenized as it descends upon each line.'''
            if x > 255:
                print("Daw, Input " + repr(i+1) + " is not in range.  It must be greater than 255.")
            elif x < 0:
                print("Daw, Input " + repr(i+1) + " is not in range.  It must be less than 0.")
            else:
                print("Yep! Input " + repr(i+1) + " is correct. Noice!")


            '''This now increments the counter. (Could be placed ahead of if
                statement but then repr(i+1) would not need +1.)'''
                
            i = i + 1
            

#Except excludes non integers if there is an error in the program.
            
except ValueError:
    print("Whoops! Looks like there is an error since the IP Address input has letters in the input seen as follows " + repr(i+1) + ". Retry if you can, thanks.")
