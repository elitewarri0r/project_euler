'''

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

'''

number = 100
op = 1
# Adding all the numbers
for x in range(1,number + 1 ) :
    op = op * x
    
# adding all the digihts     
addition = sum(list(str(op)))
print(addition,'is the sum of the digits in the number 100!')
