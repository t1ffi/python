#Tiffi Westcott
#While loops

first = input('Please enter the first term: ')
last = input('Please enter the last term: ')
interval = input('Please enter the interval between terms: ')

sum = 0
i = int(first)

while i <= int(last):
    sum = sum + i
    i = i + int(interval)
print 'sum = '+ str(sum)
