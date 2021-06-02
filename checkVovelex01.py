l=['a','e','i','o','u']
s=input("Enter any string :")
count=0
for i in range(len(l)):
    count=0
    for j in range(len(s)):
        if s[j].lower()==l[i]:
            count+=1
    print(l[i],' is occured in : ',count)