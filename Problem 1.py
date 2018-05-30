# Find the sum of all the multiples of 3 or 5 below 1000.

print ('problem 1')
input2 = 1000
output = 0
input1 = int(input2)
for x in range (1,input1+1) :
    three = x%3
    five = x%5
    if five == 0 or three == 0 :
        output = output + x

print (output)

