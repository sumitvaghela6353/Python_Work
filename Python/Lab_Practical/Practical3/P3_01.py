#------------using Iterative------------#

def iterativeFact(m):
     factorial = 1
     if  m >= 1:
          for i in range (1, int(m)+1):
               factorial = factorial * i
          return factorial

#------------using Recursion------------#

def rec_fac(n):
     if n == 1 or n == 0:
          return 1
     elif n < 0:
          return ('Not Applicable')
     else:
          return n*rec_fac(n-1)
num = int(input('Enter a number: \n'))
print("Iterative Factotial of", num, "is", iterativeFact(num), "\n")
print("Recursive Factotial of", num, "is", rec_fac(num), "\n")


#-------------math.factorial()--------------#

# import math
# n = int(input('enter A number'))
# print(math.factorial(int(n))) 