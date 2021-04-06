#find max between 3 nos
a,b,c=eval(input("Enter 1st no : ")),eval(input("Enter 2st no : ")),eval(input("Enter 3st no : "))
if a>b:
    if a>c:
        max=a
    else:
        max=c
elif b>c:
    max=b
else:
    max=c

print(max, ' is greatest')