#Write a program to sort a dictionary by its values in descending order.
#Output: 
#Original dict :  {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
#Descending order :  {3: 4, 4: 3, 1: 2, 2: 1, 0: 0}

import operator
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print('Original dict : ',d)

desc = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
print('Descending order : ',desc)