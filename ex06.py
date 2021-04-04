#Calculate average of some elements give by user
list=[eval(x) for x in input("Enter values : ").split()]
print(list)
total=0
for i in list:
	total=total+i
avg=total/len(list)
print("Total of list : ",total)
print("Avg of list : ",avg)