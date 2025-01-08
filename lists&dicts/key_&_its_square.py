#Write a program to create a dictionary where keys are elements from a list and values are their squares.

number = int(input("Enter the list endpoint: "))
dict= {}

for x in range(1, number + 1):
    dict[x] = x ** 2
    
print("Dictionary = ", dict)