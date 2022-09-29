#  Write a program to generate dictionary of frequency of alphabets    of given string.

String = 'SBVaghela2002'
frequency = {}
for item in String:
     if item in frequency:
          frequency[item] += 1
     else:
          frequency[item] = 1
print(frequency)
