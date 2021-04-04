#Calculate total of square-root elements give by user
import math as m
list=[eval(x) for x in input("Enter values : ").split()]
print(list)
total=0
for i in list:
	total=total+m.sqrt(i)
print("Total of list : ",total)