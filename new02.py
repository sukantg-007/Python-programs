import math as m
print('x^4+x^3+x^2+x+1 evaluate' )
x=int(input('Enter value of x:'))
y=int(input('Enter max power:'))
sum=0
for i in range(y+1):
    if i==0:
        print('1',end=' + ')
    else:
        print(x,'^',i,end=' + ')
    sum=sum+m.pow(x,i)
print()
print("Result:",sum)

