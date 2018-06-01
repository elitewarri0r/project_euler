'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
'''
import math
def isPrime(ip)  :
    output = 1
    ip1 = int(ip)
    
    if ip1 == 2 or ip1 == 3 :
        output = 1
    elif ip1 % 2 == 0 or ip1 == 1 :
       output = 0
    
    else :
        ip2 = math.sqrt(ip1)
        ip3 = math.ceil(ip2) + 1
        for x in range(3,ip3) :
            if ip1 % x == 0 :
                output = 0
    return output

checker = 0
ouputa = 0
# When this loop runs we finds the primes and when we get the 10 001 st one we will print it
for x in range(2,1000000000) :
    if isPrime(x) == 1 :
        checker = checker  + 1
    # Here we check if it is the 10001 st prime
    if checker == 10001 :
        outputa = x
        break

print(outputa,'is the 10 001 st prime number')
