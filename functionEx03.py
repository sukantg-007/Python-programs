#find reverse of given input
def reverseVal(n):
    rev=0           
    if n%10==n:
        return n
    elif n==10:
        return '01'
    else:
        while n>0:
            rev=rev*10+n%10
            n=n//10
        return rev    


print(reverseVal(int(input("Enter any number : "))))