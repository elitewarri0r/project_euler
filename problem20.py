'''

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

'''

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
