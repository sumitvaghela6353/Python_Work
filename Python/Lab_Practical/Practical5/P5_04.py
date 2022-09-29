# Write a Python program to sum all the items in a dictionary.
def Sum(item):
   sum = 0
   for i in item.values():
      sum = sum + i
   return sum
item = {'a':100, 'b':200, 'c':300}
print(Sum(item))
