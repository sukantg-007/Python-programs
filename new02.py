# k=1
# for i in range(1,5):
#      for j in range(1,5):
#         if (j<=i):
#             print("",k,end='\t')
#             k=k+1
#      print()

k=1
for i in range(1,5):
    for j in range(4,0,-1):
        if(j>=i):
            print("",k,end='\t')
            k=k+1
    print()        