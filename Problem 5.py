
totalsq = 0
eachsq = 0

for x in range(1,101) :
    totalsq = totalsq + x
    eachsq = eachsq + (x*x)

totalsq = totalsq * totalsq
print(totalsq)
print(eachsq)
output = totalsq - eachsq

print ('The final output is ',output)
