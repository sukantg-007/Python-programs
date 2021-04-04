#average of five numbers from command prompt
from sys import argv
print('Original List : ',argv)
list=[int(x) for x in argv[1:]]
print('New List : ',list)
add=0
for i in list:
	add=add+i

avg=add/len(list)

print('Average of list :',avg)
