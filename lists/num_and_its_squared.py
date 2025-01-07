#Number and its square
#x= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Create a list of tuples where each tuple contains a number and its square for numbers from 1 to 10.
squared_numbers = [(x, x**2) for x in range(1, 11)]
print("Squared numbers: ",squared_numbers)
