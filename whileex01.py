x=123
rev=0
while x>0:
    r=x%10
    x=x//10
    rev=rev*10+r

print("Reverse of number : ",rev)