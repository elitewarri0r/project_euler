'''
This function can convert any number into binary
'''

import math
def binNum(num):
    quotient = 0
    quotient = math.floor(num/2)
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
 
