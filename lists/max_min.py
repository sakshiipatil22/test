#Write a program to find the maximum and minimum element in a list without using the built-in max() and min() functions.
#Output:
#Enter the list of elements: 3 2 5 8 9
#List is:  ['3', '2', '5', '8', '9']
#Maximum value is:  9
#Minimum value is :  2


list=(input("Enter the list of elements: ")).split()
print("List is: ", list)

max= list[0] 
min=list[0] 

for num in list:
    if num > max:
        max = num
    if num < min:
        min = num

print("Maximum value is: ", max) 
print("Minimum value is : ", min) 
