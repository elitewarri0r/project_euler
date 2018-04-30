
# problem three
# the isPrime function
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
        #print ('ip3', ip3)
    for x in range(3,ip3) :
            #print ("its x",x)
            if ip1 % x == 0 :
                #print ("Y")
                output = 0
    return output
# end of the isPrime funtion

inp = input('no. : ')
inp251 = int(inp) #inp25 is numerical input
#inp25 = math.sqrt(inp251)
#inp3 = math.ceil(inp25)
inp3 = inp251/2
inp3 = math.ceil(inp3)
# print(inp3,inp251)

for x in range(inp3, 0, -1) :
    isp = isPrime(x)
    #print (isp,' and ',x)
    if isp == 1 :
        #print ('yea got in')
        if inp251%x == 0 :
            #print ('the isp is ',isp, 'and', x)
            print('the highest prime factor of ',inp251,'is ',x)
            break
  

