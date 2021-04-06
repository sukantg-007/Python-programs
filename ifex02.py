#find greatest number among two numebrs
a,b=input("Entet two numbers : ").split()#10 20
a=int(a)
b=int(b)
if a>b:
    print(a,' is greater than ',b)
else:
    print(b,' is greater than ',a)