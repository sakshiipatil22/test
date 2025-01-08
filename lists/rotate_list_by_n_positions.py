#Implement a program to rotate a list by n positions to the right.
# Output: [4, 5, 6, 1, 2, 3]
from collections import deque


a=[]
n=int(input("Enter number of elements: "))
for i in range(1,n+1):
    b=int(input("Enter elements: "))
    a.append(b)
pos=int(input("Enter the position to be rotated from: "))   
#list_1 = [1, 2, 3, 4, 5, 6]
deque_1 = deque(a)

deque_1.rotate(pos)

a= list(deque_1)

print("The rotated list is : ",a) 
