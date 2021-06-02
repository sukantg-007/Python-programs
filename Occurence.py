s='learn python to learn coding learn to find learn and get learn to know learn'
s1='learn'
begInd=-1
index=0

while True:
    index=s.find(s1,begInd+1, len(s))    
    if index==-1:
        break    
    print(s1,' present at index : ',index)
    begInd=index