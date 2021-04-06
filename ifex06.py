#find max between 3 nos
a,b,c,d=eval(input("Enter 1st no : ")),eval(input("Enter 2st no : ")),eval(input("Enter 3st no : ")), eval(input("Enter 3st no : "))
if a>b:
    if a>c:
        if a>d:
            max=a
        else:
            max=d
    elif c>d:
        max=c
    else:
        max=d

elif b>c:
    if b>d:
        max=b
    else:
        max=d
elif c>d:
    max=c
else:
    max=d

print(max, ' is greatest')