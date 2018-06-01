# Find the sum of all the multiples of 3 or 5 below 1000.

print ('problem 1')
output = 0
input1 = int(input('enter a number : '))

# When this loop runs we pick all the multiples of 3 or 5
for x in range (1,input1) :
    three = x%3
    five = x%5
 
    if five == 0 or three == 0 :
        # If x is a multiple of 3 or 5 we add it to the output
         output = output + x

print (output,'is the sum of all the multiples of 3 or 5 below 1000.')


