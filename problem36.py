'''
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)

'''

import math
def tobinary(num):
    quotient = 0
    if num % 2 == 0 :
        base2 = '0' 
    else :
        base2 = '1' 
    while quotient !=1 :
        quotient = math.floor(num/2)
        if quotient % 2 == 0 :
            base2 = '0' + base2
        else :
            base2 = '1' + base2
        num = quotient
        
    base2 = int(base2)
    return base2
 

def palindrome(num):
    if num[::-1] == num:
       return 1
    else:
       return 0
    
count = 0

for x in range(1000001) :
    xa = str(x)
    if palindrome(xa) == 1 :
        xb = tobinary(x)
        xa = str(xb)
        xa = xa[2:]
        if palindrome(xa) == 1 :
            count = count + x
            
print(count)
