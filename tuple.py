>>> t=(10,20,30,40)
>>> type(t)
<class 'tuple'>
>>> for i in t: print(i)

10
20
30
40
>>> t[0]
10
>>> t[-1]
40
>>> t[:len(t)]
(10, 20, 30, 40)
>>> t[0]=100
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    t[0]=100
TypeError: 'tuple' object does not support item assignment
>>> t[:]
(10, 20, 30, 40)
>>> t.append(10)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    t.append(10)
AttributeError: 'tuple' object has no attribute 'append'
>>> list=[10,10.25,'python',10+20j,True]
>>> t=tuple(list)
>>> t
(10, 10.25, 'python', (10+20j), True)
>>> list.append(10)
>>> list
[10, 10.25, 'python', (10+20j), True, 10]
>>> t=tuple(list)
>>> t
(10, 10.25, 'python', (10+20j), True, 10)
>>> t[-1]
10
>>> for i in t:
	print(i)

	
10
10.25
python
(10+20j)
True
10
>>> t.remove(10)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    t.remove(10)
AttributeError: 'tuple' object has no attribute 'remove'
>>> 