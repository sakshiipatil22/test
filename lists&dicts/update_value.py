#Create a Python program to update the value of a dictionary if its key exists in a given list.

test_dict = {'gfg' : [1, 5, 6], 'is' : 2, 'best' : 3}

print("The original dictionary : " + str(test_dict))

temp={'gfg':[x * 2 for x in test_dict['gfg']]}
test_dict.update(temp)
	

print("Dictionary after updation is : " + str(test_dict))