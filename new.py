space=' '
k=0
s="ABCDEGHIJKL"
for i in range (1,6):
    for j in range(1,6):
        if (j>=i):
            if k<=len(s)-1:
                print(s[k],end=" ")
                k=k+1
            else:
                print("*",end=" ")
                k=k+1
        
        else:
            print(space,end=' ')
    print()