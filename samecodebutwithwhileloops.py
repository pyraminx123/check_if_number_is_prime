import sys
from os import system
from time import sleep

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
  
loop = True


while loop == True:
  try:
    num = int(input("Input a number to check if it's prime: "))
  except ValueError:
    print("Error: an int is required here.")
    sys.exit()
    
  check(num)
  secloop = True
  
  while secloop == True:
    print()
    answer = input("Do you want to check another number? [y/n]: ").lower()


    if answer == "y":
      loop = True
      secloop = False
      system("clear")
    elif answer == "n":
      sys.exit()
    else:
      print("Sorry the letter y or n is required here.")
      sleep(1)
      loop = False
      system("clear")
