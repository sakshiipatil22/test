#Create a program to count the frequency of characters in a given string using a dictionary
#Output: Frequency count of each element in dict is:  {1: 1, 2: 1, 3: 1, 5: 1, 6: 1, 7: 1, 8: 1}
#s = input()


a={1, 3, 5, 6, 7, 3, 1, 2, 8, 7}
dict = {} 
  
for i in a: 
    if i in dict: 
        dict[i] += 1
    else: 
        dict[i] = 1

print("Frequency count of each element in dict is: ",dict)