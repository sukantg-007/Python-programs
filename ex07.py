#Calculate total of square elements give by user
import math as m
list=[eval(x) for x in input("Enter values : ").split()]
print(list)
total=0
for i in list:
	total=total+m.pow(i,2)
print("Total of list : ",total)