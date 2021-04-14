>>> list=[10,20,30,40]
>>> list
[10, 20, 30, 40]
>>> for i in list:print(i)

10
20
30
40
>>> list=[10,10.25,'python',10+20j,True]
>>> list
[10, 10.25, 'python', (10+20j), True]
>>> for i in list:print(i)

10
10.25
python
(10+20j)
True
>>> list[2]
'python'
>>> list[1]='numpy'
>>> for i in list: print(i)

10
numpy
python
(10+20j)
True
>>> list
[10, 'numpy', 'python', (10+20j), True]
>>> list[-1]
True
>>> list[1:]
['numpy', 'python', (10+20j), True]
>>> len(list)
5
>>> list[:4]
[10, 'numpy', 'python', (10+20j)]
>>> list[5]
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    list[5]
IndexError: list index out of range
>>> list[:5]
[10, 'numpy', 'python', (10+20j), True]
>>> list[:len(list)]
[10, 'numpy', 'python', (10+20j), True]
>>> list[:6]
[10, 'numpy', 'python', (10+20j), True]
>>> list[6]
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    list[6]
IndexError: list index out of range
>>> list[:10]
[10, 'numpy', 'python', (10+20j), True]
>>> list[-3:]
['python', (10+20j), True]
>>> list[-6]
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    list[-6]
IndexError: list index out of range
>>> list[-6:]
[10, 'numpy', 'python', (10+20j), True]
>>> 