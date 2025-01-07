#Implement a program to rotate a list by n positions to the right.

def rightRotate(lists, num):
	output_list = []
	
	for item in range(len(lists) - num, len(lists)):
		output_list.append(lists[item])

	
	for item in range(0, len(lists) - num):
		output_list.append(lists[item])

	return output_list

a=(input("Enter the elements in the list:")).split()
print("List is :",a)
n=(input("Enter the rotate number:"))
print("Rotate number: ",n)
#rotate_num = 3
#list_1 = [1, 2, 3, 4, 5, 6]

print(rightRotate(a, n))