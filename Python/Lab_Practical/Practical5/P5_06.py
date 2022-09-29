n = int(input("Enter number of student: "))
result = {}
for i in range(n):
     print("Enter Details of Student: ", i+1)
     r_no = int(input("r_no :"))
     name = (input("name :"))
     cpi = float(input("cpi :"))
     result[r_no] = [name, cpi]
print(result)
for student in result:
     if result[student][1] > 9:
          print(result[student][0])
  