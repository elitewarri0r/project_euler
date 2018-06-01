
'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''


op = 0
opc = 0

# When this loop runs we fish out the number
for x in range(1,300000000 ) :
    opc = 0
    # Checking if the number is dvivsable by all number 1 to 20
    for z in range(1,21) :
        if x%z == 0 :
            opc = opc + 1
    # Checking if the number is the answer
    if opc == 20 :
        print('hello')
        op = x
        break

print(op,'is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20.')
