p='abcd4534'
s='a4%b5&c6-d7*'
print(p.isalnum())
s1=''
s2=''
s3=''
for i in s:
    if i.isalpha():
        s1=s1+i
    elif i.isdigit():
        s2=s2+i
    else:
        s3=s3+i
print(s1+s2+s3)