def allFunction(x,y):
    a=x+y
    s=x-y
    m=x*y
    d=x/y
    f=x//y
    md=x%y
    return a,s,m,d,f,md

t=allFunction(20, 10)
a,s,m,d,f,md=t
print('Addition     : ',a)
print('Substrac     : ',s)
print('Multiply     : ',m)
print('Divide       : ',d)
print('Floor        : ',f)
print('Modulus      : ',md)
