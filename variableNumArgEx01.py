def add(*n):
    if len(n)==0:
        sum=0
    else:
        sum=1
    for i in n:
        sum*=i
    return sum

print(add())
print(add(10))
print(add(10,20))
