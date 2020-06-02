# more python tricks

#----- x = (y>4)?2:3 equivalent

y = 2 
x = 2 if (y>4) else 3
print (x)

#------  for tricks
for line in ['d','o','g','s']:
    print(line,end = '')
print(' are great')

dogs = ['d','o','g','s']
for i,letter in enumerate(dogs):
    print('%d: %s' % (i,letter))

list(enumerate(dogs))  # turns it into an array of tuples

test = [(1,1),(2,1),(3,2)]
for i,j in test:
	print('%d: %d' % (i,j))

#------ cool tricks from geeksforgeeks
x, y = 10, 20
print(x, y) 
x, y = y, x # swaps two values in one line
print(x, y)

a = ["Geeks", "For", "Geeks"] 
print(" ".join(a))   # makes one string

n = 10
result = 1 < n < 20
print(result) 
result = 1 > n <= 9  # crazy stuff with multiple comparisons
print(result)

import os
import socket
  
print(os) # show path to python file
print(socket)

test = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4] 
print(max(set(test), key = test.count)) # returns the most common number
