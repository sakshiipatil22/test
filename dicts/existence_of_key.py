#.Write a program to check if a key exists in a dictionary.
#Output : Exists
d = {'a': 100, 'b':200, 'c':300}

if d.get('b') == None:
  print("Not Exist")
else:
  print("Exists")