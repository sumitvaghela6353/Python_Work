#------------------Without Function------------------#
num_1 = int(input('Enter your first number: '))
num_2 = int(input('Enter your second number: '))
 
print('Select operation')
print('1.addition')
print('2.subtraction')
print('3.multiplication')
print('4.division')

choice = int(input('select operarion from 1,2,3,4:')) 
 
# num_1 = int(input('Enter your first number: '))
# num_2 = int(input('Enter your second number: '))
 
if choice == 1:
    print(num_1 + num_2)
 
elif choice == 2:
    print(num_1 - num_2)
 
elif choice == 3:
    print(num_1 * num_2)
 
elif choice == 4:
    print(num_1 / num_2)
 
else:
    print('Invalid Choice')


#------------------using Function------------------#
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# def add(a, b):
#      return a + b

# def sub(a, b):
#      return a - b

# def mult(a, b):
#      return a * b

# def div(a, b):
#      return a / b

# print('Select operation')
# print('1.addition')
# print('2.subtraction')
# print('3.multiplication')
# print('4.division')

# choice = int(input('select operarion from 1,2,3,4:'))    

# if choice == 1:
#      # add = a + b
#      print('addition of Two Number', add(a,b))
     
# elif choice == 2:
#      # sub = a - b
#      print('subtraction of Two Number', sub(a,b))

# elif choice == 3:
#      # mult = a * b
#      print('multiplying of Two Number', mult(a,b))

# elif choice == 4:
#      # div = a / b
#      print('divide of Two Number', div(a,b))
     
# else:
#      print("Invalid choice")