x = [[5,2,1], 
     [3,6,2], 
     [2,6,1]]

y = [[4,8,9], 
     [2,5,1], 
     [5,3,8]]

result = [[0,0,0], [0,0,0], [0,0,0]]

# addition
for i in range(len(x)):
     for j in range(len(x[0])):
          result[i][j] = x[i][j] + y[i][j]
for r in result:
     print(r)  
   
#multication  

result1  = [[0,0,0], [0,0,0], [0,0,0]]
for i in range(len(x)):
     for j in range(len(y[0])):
          for k in range(len(y)):
               result1[i][j] += x[i][k] * y[k][j]
for r in result1:
     print(r)