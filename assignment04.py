import math as m
print("Evaluate series : x+x^3/3!+x^5/5!+..+x^n/n!")
x=int(input("Enter value of x : "))
y=int(input("Enter Last Power : "))
sum=0
for i in range(1,y+1,2):
    if i==1:
        print(x,end="")
    else:
        print(" + ",x,"^",i," / ",i,"!",end="")
    sum=sum+(m.pow(x,i)/m.factorial(i))

print("Result is : ",sum)
