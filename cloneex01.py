#assinging other ref to single objec
x=10
y=x
print(x is y)

#way1---slice operator
x=[10,20,30,40]
y=x[:]
print(x is y)
print('Old x: ',x)
print('Old y: ',y)
y[1]=100
print('New x: ',x)
print('New y: ',y)

#way2: copy() function
x=[10,20,30,40]
y=x.copy()
print(x is y)
print(x)
print(y)
y[1]=100
print(x)
print(y)