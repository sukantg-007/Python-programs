for i in range(5):
    for j in range(5):
        if j==3:
            continue # it will skip 5
        print(j,end=' ')
    print()

'''
output
continueEx02.py
0 1 2 4
0 1 2 4
0 1 2 4
0 1 2 4
0 1 2 4
'''