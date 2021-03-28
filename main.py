import sys

try:
  num = int(input("Input a number to check if it's prime: "))
except ValueError:
  print("Error: an int is required here.")
  sys.exit()

def prime(number):
  global count
  count = 0
  for i in range(2, number):
    if (number % i) == 0:
      print(i, "X", int(number/i), "=", number)
      count += 1

def check(number):
  prime(number)
  if count > 0:
    print(number, "is not a prime number")
  else: 
    print(number, 'is a prime number')
  
check(num)
