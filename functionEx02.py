def factorial(n):
    fact=1
    while n>=1:
        fact=fact*n
        n=n-1
    return fact

a=eval(input("Enter a number : "))
for i in a:
    print('Factorial of {} : {}'.format(i,factorial(i)))
