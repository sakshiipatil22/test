#Write a program to find all the unique elements in a list.


#a=(input("Enter the elements in the list: ")).split()
#print("List is: ",a)

#unique_elements_list = list(dict.fromkeys(a))

#print("The list containing unique elements is :",unique_elements_list)

a=[1, 1, 3, 5, 3, 6, 5, 6, 7]
unique = []


for x in a:
    if x not in unique:
        unique.append(x)

print("List of unique elements is :",unique)
