fa = 1
fb = 1
equal = 0
op = 0
count = 2

while 0 == 0 :
    count = count + 1
    equal = fa + fb
    equal = str(equal)
    if len(equal) == 1000 :
        op = equal
        break
    else :
        equal = int(equal)
        fa = fb
        fb = equal
        
print(op)
print('  ')
print(count)
