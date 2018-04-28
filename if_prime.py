#if prime
def ifprime (ip = input('Enter a number and it will checked if it is a prime : '))  :
    
    output = 0
    ip1 = int(ip)
    
    if ip1%2 == 0 and ip1 != 2 :
       output = 0       
       break
    
    else :
        checker = 1
        import math
        ip2 = math.sqrt(ip1)
        ip3 = math.ceil(ip2)
        
        for x in range(1,ip3) :
            z = ip1%x
            if z == 0 :
                checker = checker + 1
                
        if checker == 2 :
            output = 1
            break
        else :
            output = 0
            break
    return output

for x in range(10) :
    ifprime(x)
    
