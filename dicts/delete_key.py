#Write a Python program to remove a specific key from a dictionary

dict = {1:"xyz", 2:"abc", 3:"efg", 4:"hij"}
print("Actual dict : ",dict)
x= {}

for key, value in dict.items():
    if key!= 2:
        x[key] = value
print(x)
