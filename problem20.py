number = 100
op = 1
for x in range(1,number + 1 ) :
    op = op * x

print(op)    
op = str(op)
length = len(op)
hi = 0
addition = 0

for x in range(0,length) :
    hi = op[x]
    hi = int(hi)
    addition = addition + hi

print(addition)
