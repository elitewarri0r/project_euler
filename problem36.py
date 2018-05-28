'''
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)

'''


def palindrome(num):
    if num[::-1] == num:
       return 1
    else:
       return 0
    
count = 0

for x in range(1000001) :
    xa = str(x)
    if palindrome(xa) == 1 :
        xb = bin(x)
        xa = str(xb)
        xa = xa[2:]
        if palindrome(xa) == 1 :
            count = count + x
            
print(count)
