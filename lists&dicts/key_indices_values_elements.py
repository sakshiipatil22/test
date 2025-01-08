#Write a Python program to create a dictionary from a list where keys are indices and values are elements.
#Output: 
# Enter the elements in the list:sakshi, aditya, aditi, priya, rahul
#List is : ['sakshi,', 'aditya,', 'aditi,', 'priya,', 'rahul']
#{0: 'sakshi,', 1: 'aditya,', 2: 'aditi,', 3: 'priya,', 4: 'rahul'}


a=str(input("Enter the elements in the list:")).split()
print("List is :",a)


dictt = dict(enumerate(a))
print(dictt)