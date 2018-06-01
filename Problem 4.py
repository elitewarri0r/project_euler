
'''
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''
#problem 4
# built-in function for flipping str, x = x[::-1]

multiplier1 = int(input(" enter a number that's 3 dight : "))
multiplier2 = multiplier1
op = 0
product1 = multiplier1*multiplier2

# When this loop runs we multiply the numbers
for x in range((1000 - multiplier1)) :
    product1 = multiplier1*multiplier2
    y = str(product1)
    # Here we flip the product and check if it is a palindrome or not
    z = (y[::-1])
    if z == y :
        op = product1
    multiplier1 = multiplier1 + 1
    multiplier2 = multiplier2 + 1
  

print(op,'is the largest palindrome made from the product of two 3-digit numbers.')
