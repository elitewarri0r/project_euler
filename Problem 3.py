
# problem three

ip = 12345
ifprime = 0
highestp = 2
op = 0
opC = 0
while 0==0 :
    opC = op
    for x in range(1,(ip+1)) :
        if ip%x == 0 :
            ifprime = ifprime + 1
    if ifprime == 2 :
        print ('The input is prime')
        ifprime = 0
        break
    else :
        for x in range(0,ip) :
            for z in range (1,x+1) :
                if x%z == 0 :
                    ifprime = ifprime + 1
            if ifprime == 2 and x > 1 :
                highestp = x
                print (highestp)
            if ip%highestp == 0 :
                op = highestp
    print (op)
    if opC == op :
        break 

