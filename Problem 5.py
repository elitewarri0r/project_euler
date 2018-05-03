
'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
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
