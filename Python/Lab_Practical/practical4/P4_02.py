my_list = [20,10,10,30,10,20,30,40,40,50]
frequency = {}
for item in my_list:
     if item in frequency:
          frequency[item] += 1
     else:
          frequency[item] = 1
print(frequency)
print("\n")

#-------------use import  and method-------------#

import collections

my_list2 = [5,10,10,5,15,20,5,20,30,15,30]
frequency2 = collections.Counter(my_list2)
print(dict(frequency2))