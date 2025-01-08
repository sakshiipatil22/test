#Second largest number from the list
#Output: Second largest element is : 89
import heapq

a = [10, 20, 4, 45, 90, 89]
#a=(input("Enter the elements in the list:")).split()
#print("List is :",a)

# Get the two largest numbers using heapq.nlargest
top_two = heapq.nlargest(2, a)


print("Second largest element is :",top_two[1])


