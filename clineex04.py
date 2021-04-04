#seperate two list(even / odd) using command prompt
from sys import argv

list=[int(x) for x in argv[1:]]
print('Original List : ',list)

elist,olist=[],[]

for i in list:
	if i%2==0:
		elist.append(i)
	else:
		olist.append(i)

print('Even list : ',elist)
print('Odd list : ',olist)

