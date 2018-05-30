# Find the sum of all the multiples of 3 or 5 below 1000.

print ('problem 1')
output = 0
# Assigning a variable named output the value 0
input1 = 1001
# The limit for the number time the for loop should run
for x in range (1,input1) :
# A for loop that runs 1000 times
    three = x%3
    # Assigning a variable named three and giving it the reminder of x divided by 3
    five = x%5
    # Assigning a variable named three and giving it the reminder of x divided by 5
    if five == 0 or three == 0 :
    #  The if condition that checks if x is a multiple of 3 or 5   
        output = output + x
        # And if the above condition is true it adds x to the output

print (output)
# Printing the output

