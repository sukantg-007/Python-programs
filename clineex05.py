#seperate two list(even / odd) using command prompt
from sys import argv

list=argv[1:]

for i in list:
	print(i,'	:	',type(eval(i)))

'''
vedanta-pc02@vedantapc02-HP-Compaq-dc7800p-Small-Form-Factor:~/Desktop/python-prog/Kate$ python3 clineex05.py 10 10.25 \"python\" 10+2j True
10 	:	 <class 'int'>
10.25 	:	 <class 'float'>
"python" 	:	 <class 'str'>
10+2j 	:	 <class 'complex'>
True 	:	 <class 'bool'>

'''
