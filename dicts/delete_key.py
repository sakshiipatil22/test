#Write a Python program to remove a specific key from a dictionary
# Output: {'a': 1, 'c': 3}

dict = {'a': 1, 'b': 2, 'c': 3}
for key in list(dict.keys()):  
    if key == 'b':
        del dict[key]
print(dict)