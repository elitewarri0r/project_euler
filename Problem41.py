'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
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
        #print ('ip3', ip3)
        for x in range(3,ip3) :
            if ip1 % x == 0 :
                output = 0
    return output

number = 50 
for x in range(1000000000) :
    print(number)
    if isPrime(number) == 1 :
        num = sorted(list(str(number)))
        l = len(num) 
        for x in range(l) :
            if num[x] is x+1 :
                if x == l :
                    print(number)
            else :
                break
    number = number + 1
