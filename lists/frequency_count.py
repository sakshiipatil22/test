#.Write a program to find the frequency of each element in a list
#Output: The frequency of each element is :  {12: 1, 23: 2, 45: 2, 34: 1, 77: 1}

#a=(input("Enter the list of element: ")).split()
#print("List is : ",a)

a = [12, 23, 23, 45, 34, 45,77]
frequency = {}


for item in a:
  
   if item in frequency:
      frequency[item] += 1
   else:
      frequency[item] = 1

print("The frequency of each element is : ",frequency)

