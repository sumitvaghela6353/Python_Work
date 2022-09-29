# Write a program to invert keys and values of dictionary.

mydict = ({'name': 'Sumit', 'id': 'sbv#02', 'dob': '14/11/2002'})
print('Initial Dictionary', mydict)
inv_dict = {v:k for k,v in mydict.items()}
print('Inverted Dictionary', inv_dict)
