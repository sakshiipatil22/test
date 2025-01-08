#Write a program to invert a dictionary (swap keys and values).

dict={1:"sakshi", 2:"soham", 3:"aditya", 4:"arya"}

rev_dict={}

for key,value in dict.items():
    rev_dict[value]=key
    print("Inverted dict is: ",rev_dict)