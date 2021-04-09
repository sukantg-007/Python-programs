print("Fibonachi series : 1,1,2,3,5,8..")
limit=int(input("Enter limit :"))
x=1
y=1
for i in range(limit-1):
    if i==0:
        print(x,end="")
    else:
        print(",",x,end="")
    temp=x
    x=y
    y=y+temp