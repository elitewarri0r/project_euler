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

for x in range(2,99999999999999999999) :
    if isPrime(x) == 1 :
        checker = checker  + 1
        #print(checker)
    if checker == 10001 :
        outputa = x
        break

print(outputa)
