#Create a Python program to group a list of numbers into even and odd using a dictionary.
#Output: Enter number of elements: 5
#Enter element: 3
#Enter element: 4
#Enter element: 6
#Enter element: 8
#Enter element: 1
#Even list is:  [4, 6, 8]
#Odd list is : [3, 1]

a=[]
n=int(input("Enter number of elements: "))
for i in range(1,n+1):
    b=int(input("Enter element: "))
    a.append(b)

even=[]
odd=[]

for j in a:
    if (j%2==0):
        even.append(j)
    else:
        odd.append(j)

print("Even list is: ",even)
print("Odd list is :",odd)