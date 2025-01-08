#Write a Python program to update a dictionary with another dictionary's keys and values.
# output
#The original dictionary 1 is : {'gfg': 1, 'best': 2, 'for': 4, 'geeks': 6}
#The original dictionary 2 is : {'for': 3, 'geeks': 5}
#The updated dictionary is : {'gfg': 1, 'best': 2, 'for': 3, 'geeks': 5}

test_dict1 = {'gfg': 1, 'best': 2, 'for': 4, 'geeks': 6}
test_dict2 = {'for': 3, 'geeks': 5}


print("The original dictionary 1 is : " + str(test_dict1))
print("The original dictionary 2 is : " + str(test_dict2))

new_dict = dict(test_dict1)
new_dict.update(test_dict2)

print("The updated dictionary is : " + str(new_dict))
