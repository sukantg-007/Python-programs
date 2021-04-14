>>> list=[10,20,30,40]
>>> b=bytes(list)
>>> type(b)
<class 'bytes'>
>>> b[0]=100
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    b[0]=100
TypeError: 'bytes' object does not support item assignment
>>> list=[100,200,300,400]
>>> list
[100, 200, 300, 400]
>>> b=bytes(list)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    b=bytes(list)
ValueError: bytes must be in range(0, 256)
>>> list=['abc',10,20]
>>> list
['abc', 10, 20]
>>> b=bytes(list)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    b=bytes(list)
TypeError: 'str' object cannot be interpreted as an integer
>>> list=[256,256,256]
>>> list
[256, 256, 256]
>>> b=bytes(list)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    b=bytes(list)
ValueError: bytes must be in range(0, 256)
\
>>> b
b'\n\x14\x1e('
>>> for i in b:
	print(i)

	
10
20
30
40