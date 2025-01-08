#merging list without duplicates
#Output: Merge list without  duplicates :  [23, 45, 65, 31, 1, 89, 67, 8, 90]


list1 = [23, 45, 65, 31, 1, 89]
list2 = [67, 89, 23, 45, 8, 90]

#list1=((input("Enter first list : ")).split()
#print("List is :",list1)
#list2=((input("Enter second list : ")).split()
#print("List is :",list2)
ans = []

for data in list1:
    if data not in ans:
        ans.append(data)
        
for data in list2:
    if data not in ans:
        ans.append(data)


print("Merge list without  duplicates : ",ans)