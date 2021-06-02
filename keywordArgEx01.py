def giveMsg(name,msg):
    print("Hello ",name,msg,"!!!")

giveMsg(name='Omkar', msg='How are you')
giveMsg( msg='How are you', name='Omkar')
#giveMsg( msg='How are you', 'Omkar')#SyntaxError: positional argument follows keyword argument
giveMsg('Shubham')#TypeError: giveMsg() missing 1 required positional argument: 'msg'