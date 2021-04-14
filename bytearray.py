>>> list=[10,20,30,40]
>>> list
[10, 20, 30, 40]
>>> ba=bytearray(list)
>>> ba
bytearray(b'\n\x14\x1e(')
>>> type(ba)
<class 'bytearray'>
>>> for i in ba: print(i)

10
20
30
40
>>> ba[1]=100
>>> for i in ba: print(i)

10
100
30
40
>>> b[1]
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    b[1]
NameError: name 'b' is not defined
>>> ba[1]
100
>>> list=[256,256,256]
>>> ba=bytearray(list)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    ba=bytearray(list)
ValueError: byte must be in range(0, 256)
>>> 