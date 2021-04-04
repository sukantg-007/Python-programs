list=[int(i) for i in input("Enter values : ").split(",")]
elist=[]
olist=[]
print(list)
add=0
for x in list:
	if x%2==0:
		elist.append(x)
	else:
		olist.append(x)
	add=add+x
print('Addition of list : ',add)
print('Even list : ',elist)
print('Odd list : ',olist)
