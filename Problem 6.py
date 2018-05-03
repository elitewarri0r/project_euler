
'''
The sum of the squares of the first ten natural numbers is,
1x1 + 2x2 + ... + 10x10 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)x(1 + 2 + ... + 10) = 55x55 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


'''
totalsq = 0
eachsq = 0

for x in range(1,101) :
    totalsq = totalsq + x
    eachsq = eachsq + (x*x)

totalsq = totalsq * totalsq
print(totalsq)
print(eachsq)
output = totalsq - eachsq

print ('The final output is ',output)
