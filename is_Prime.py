import math
def isPrime(ip)  :
    output = 'false'
    ip1 = int(ip)
    
    if ip1 == 2 or ip1 == 3 :
        output = 'true'
    elif ip1 % 2 == 0 or ip1 == 1 :
       output = 'false'
    
    else :
        ip2 = math.sqrt(ip1)
        ip3 = math.ceil(ip2) + 1
        #print ('ip3', ip3)
        for x in range(3,ip3) :
            if ip1 % x == 0 :
                output = 'true'
     
for x in range(10):
    #print(x)
    isPrime(x)
