#Create a Python program to filter a list of dictionaries based on a specific key's value.
#Output:[{'name': 'sakshi', 'role': 'Engineer'}, {'name': 'rahul', 'role': 'CEO'}]

dict= [{'name': 'sakshi', 'role': 'Engineer'}, 
     {'name': 'soham', 'role': 'Manager'}, 
     {'name': 'aditi', 'role': 'Director'}, 
     {'name': 'rahul', 'role': 'CEO'}]
filter = ['Engineer', 'CEO']

key_val = []
for a in dict:
    if a['role'] in filter:
        key_val.append(a)

print(key_val)