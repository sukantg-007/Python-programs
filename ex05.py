'''
x=eval(input("Enter anything : "))
print(type(x))
'''
list=[eval(i) for i in input("Enter values : ").split()]
print(list)
for x in list:
	print(x,' : ',type(x))
