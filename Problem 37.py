'''

The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

'''
#the isPrime function 
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
# output with the example number
output = 3797
count = 1
runner = 20
#Until the number of Truncatable primes is 11 the loop repeats itself
while count < 11 :
    # if the number is a prime then only the main part of the problem starts
    if isPrime(runner) == 1 and runner != 3797 :
        runnerb = str(runner)
        #if the ending dights are not 1 then we start
        if runnerb[-1:] or runnerb[0] != 1 :
            lena = len(runnerb)
            runnerd = 2
            runnere = 2
            # the loop that checks the Truncatablity from both left and right
            while lena >= 0 and isPrime(runnerd) == 1 and isPrime(runnere) == 1:
                runnerd = runnerb[:lena]
                runnere = runnerb[-lena:]
                lena = lena - 1
        if lena == -1  :
            print(count,runner)
            output = output + runner
            count = count + 1
    runner = runner + 1

print(output)


                

