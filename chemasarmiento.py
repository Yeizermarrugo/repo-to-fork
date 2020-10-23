print("Fibonacci")
bef = 0
aft = 1
counter = 0
print(bef)
print(aft)
while counter < 13:
  next = bef + aft
  bef = aft
  aft = next
  print(aft)
  counter = counter + 1

import re
print("Primos")
def IsPrime(n):
  return re.compile(r'^1?$|^(11+)\1+$').match('1' * n) is None

counter = 0
test = 2
while counter < 15:
  if IsPrime(test):
    print(test)
    counter = counter + 1
  test = test + 1

print("Perfectos")
print("Se imprimen 4 por tiempo de ejecucuón, el 5to es 33550336")
def isPerfect(x):
  if x < 1: 
    return False
  sum = 0
  for i in range(1,x):
    if x%i==0:
      sum += i
  return sum == x
counter = 0
test = 1
while counter < 4:
  if isPerfect(test):
    print(test)
    counter = counter + 1
  test += 1
