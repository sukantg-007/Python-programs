l=[10,20,30,40]
l2=[40,50,60]
#if length is same then check whoes length is more than other
flag=False
if len(l) != len(l2):
    flag=sum(l) > sum(l2) if True else False
if flag:
    print('l is greater than l2')
else:
    print('l2 is greater than l')