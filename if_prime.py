def ifprime(ip)  :
    import math
    output = 0
    ip1 = int(ip)
    
    if ip1 == 2 or ip1 == 3 :
        output = 'true'
    elif ip1%2 == 0 or ip1 == 1 :
       output = 'false'
    
    else :
        checker = 1
        ip2 = math.sqrt(ip1)
        ip3 = math.ceil(ip2) + 1
        #print ('ip3', ip3)
        for x in range(1,ip3) :
            #print ('x', x)
            z = ip1%x
            if z == 0 :
                #print("Y")
                checker = checker + 1
                
        if checker == 2 :
            output = 'true'
        else :
            output = 'false'
    print (output)


#ifprime(9)

for x in range(10):
    #print(x)
    ifprime(x)
