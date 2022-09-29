tuple_list = [(2, 5), (3, 6), (4, 2), (5, 3), (6, 1)]
print("The original list is:", str(tuple_list))

result1 = list(map(max, zip(*tuple_list)))
result2 = list(map(min, zip(*tuple_list)))

print("The max value:",  str(result1))
print("The min value:",  str(result2))
