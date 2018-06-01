'''
This function can convert any number into binary
'''

import math
def binNum(num):
     num = num*2
    quotient = 0

    while quotient !=1 :
        # We divide the input by two 
        quotient = math.floor(num/2)
        # And if the quotient is a even number we add '0' to the ouput or '1' if its odd
        if quotient % 2 == 0 :
            base2 = '0' + base2
        else :
            base2 = '1' + base2
        num = quotient
        
    base2 = int(base2)
    return base2
 
