a=int(input('Number'))
# n=0
sum=0
while(a!=0):
     n = a % 10
     sum = sum + n
     a = a // 10
print(sum)

# s = sum([int(i) for i in str(a)])
# print(s)