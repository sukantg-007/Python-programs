def smartDec(function):
    def inner(a,b):
        if b==0:
            print('Cant divide by zero')
        else:
            return function(a,b)
    return inner

@smartDec
def division(a,b):
    return a/b

print(division(10,2))
print(division(10,5))
print(division(10,0))