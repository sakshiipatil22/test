#even_num_using list comprehension
a = [2, 4, 2, 5, 5, 1, 8, 7, 6, 4]
#a=(input("Enter the elements in the list:")).split()
#print("List is :",a)


even_num = [val for val in a if val % 2 == 0]
print("List of even numbers using list comprehension: ",even_num)
