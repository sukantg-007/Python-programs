l=[40,50,60]
l2=[50,60,40]
count=0
for i in range(len(l)):
    for j in range(len(l)):
        if l[i] == l2[j]:
                count+=1

if count == len(l):
    print("Both are same")
else:
    print("Not same")