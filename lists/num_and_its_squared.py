#Number and its square
#Output: Squared numbers:  [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36), (7, 49), (8, 64), (9, 81), (10, 100)

#x= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Create a list of tuples where each tuple contains a number and its square for numbers from 1 to 10.
squared_numbers = [(x, x**2) for x in range(1, 11)]
print("Squared numbers: ",squared_numbers)
