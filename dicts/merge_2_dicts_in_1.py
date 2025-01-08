#Write a program to merge two dictionaries into one.

a={1:"Sakshi", 2:"Aditya", 3:"Sejal"}
b={4:"Rahul", 5:"Anisha", 6:"Sarthak"}

#print("Merging two dictionaries : ", a|b )
a.update(b)
print("Merging two dictionaries : ",a)