#without default args
'''
def add(x,y):
    return x+y

add(10)#TypeError: add() missing 1 required positional argument: 'y'
'''
#with default args
'''
SyntaxError: non-default argument follows default argument
def add(x=0,y):
    return x+y

print(add(10))
'''
def add(x,y=0):
    return x+y

print(add(10))
print(add())