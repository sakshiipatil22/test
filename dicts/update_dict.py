#Write a Python program to update a dictionary with another dictionary's keys and values.

to_update ={}

dict_list = [
    {"name": "Sakshi", "age": 25},
    {"city": "New York"}
]

for dictionary in dict_list:
    to_update.update(dictionary)

print("Updated Dictionary:", to_update)