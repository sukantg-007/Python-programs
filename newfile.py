# s='python lengague'
# c=0
# for x in s:
#     print('index:{} \tCharacter:{}'.format(c,x))
#     c=c+1
# list=[10,20,30,40,50]
# for i in list:
    # print(i,end=",")
# import math as m
# list=[eval(x) for x in input("Enter values : " ).split() ]
# print(list)
# total=0
# for i in list:
#     total=total+m.pow(i,2)
# print("Total of list : ",total)    
import math as m
list=range(1,11)
for i in list:
    print (i)
# list=[eval(x) for x in input("Enter values : " ).split() ]
print(list)
sqlist=[]
total=0
for i in list:
    sqlist.append(int(m.pow(i,2)))
    total=total+m.pow(i,2)
print(sqlist)
print("Total of list : ",total)
