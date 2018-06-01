
'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''

import math
def isPrime(ip)  :
    output = 1
    ip1 = int(ip)
    
    # if input is 2 or 3 the output will become positive
    if ip1 == 2 or ip1 == 3 :
        output = 1
        
    # if input is a even-valued term or 1 the output will become negative 
    elif ip1 % 2 == 0 or ip1 == 1 :
       output = 0
    
    else :
        ip2 = math.sqrt(ip1)
        ip3 = math.ceil(ip2) + 1
        
    # When this loop runs we will divide the number to see if it has any factors  
    for x in range(3,ip3) :
            if ip1 % x == 0 :
                output = 0
    return output

inp = int(input('enter a number : '))
inp251 = int(inp) 
inp3 = inp251/2
inp3 = math.ceil(inp3)

# When this loop runs backwards we will find the prime that can divide the input
for x in range(inp3, 0, -1) :
    isp = isPrime(x)
    
    if isp == 1 :
        
        if inp251%x == 0 :
            print('The highest prime factor of ',inp251,'is ',x)
            break
  

