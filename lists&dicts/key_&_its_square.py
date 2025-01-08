#Write a program to create a dictionary where keys are elements from a list and values are their squares.
#Output: Enter the list endpoint: 5
#Dictionary =  {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


number = int(input("Enter the list endpoint: "))
dict= {}

for x in range(1, number + 1):
    dict[x] = x ** 2
    
print("Dictionary = ", dict)