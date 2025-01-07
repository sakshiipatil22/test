a=(input("Enter the list of element: ")).split()
print("List is : ",a)

#random_list = [12, 23, 23, 45, 34, 45,77]
frequency = {}


for item in a:
  
   if item in frequency:
      frequency[item] += 1
   else:
      frequency[item] = 1

print("The frequency of each element is : ",frequency)

