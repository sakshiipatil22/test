#Create a program to find the dictionary with the highest value for a specific key in a list of dictionaries.
#Output: The key with the maximum value is:  4
 

#a=(input("Enter the elements in the list:")).split()
#print("List is :",a)
   
dict = {'1': 100, '2': 200, '3': 300, '4':400}  
   
Key_max = max(zip(dict.values(), dict.keys()))[1]  
print("The key with the maximum value is: ", Key_max) 