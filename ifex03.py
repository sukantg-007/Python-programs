list=[eval(x) for x in input("Enter values : ").split()]
olist, elist=[],[]
for i in list:
    if i%2==0:
        elist.append(i)
    else:
        olist.append(i)

for e in elist:
    print(e, ' is even')
for o in olist:
    print(o, ' is odd')