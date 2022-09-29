def pascalsTriangle():
     height = int(input("Enter height of triangle:"))
     t_List = []
     for R in t_List(0, height + 1):
          n_List = []
          if R == 0:
               n_List = [1]
          elif R == 1:
               n_List == [1, 1]
          else:
               for C in R:
                    if C == 0:
                         n_List.append(1)
                    elif C == R:
                         n_List.append(1)
                    else:
                         A = t_List()
     print(pascalsTriangle(t_List))
