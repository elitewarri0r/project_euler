# project_euler
Python coding for tasks from project euler : https://projecteuler.net/archives

print (" If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.")

T = 0
F = 0 
t = 0
f = 0
s = 0

while t < 1000 :
  t = 3 * T
  s = s + t
  T = T + 1
 
while f < 1000 :
  f = 5 * F
  s = s + f
  F = F + 1

print ("the sum of all the multiples of 3 or 5 below 1000 is,",s)
