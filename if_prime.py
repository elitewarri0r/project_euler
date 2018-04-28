#if prime
def ifprime(ip)  :
    output = 0
    ip1 = int(ip)
    if ip1%2 == 0 and ip1 != 2 :
       output = 'false'       
    
    else :
        checker = 1
        import math
        ip2 = math.sqrt(ip1)
        ip3 = math.ceil(ip2)
        
        for x in range(1,ip3+1) :
            z = ip1%x
            if z == 0 :
                checker = checker + 1
                
        if checker == 2 :
            output = 'true'
        else :
            output = 'false'
    print (output)

    for x in range(11) :
        ifprime(x)
