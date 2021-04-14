list data type:

>>> list=[10,20,30,40]
>>> type(list)
<class 'list'>
>>> list.append(50)
>>> list
[10, 20, 30, 40, 50]
>>> list.remove(20)
>>> list
[10, 30, 40, 50]
>>> list=[10,20,['abc','def','ghi'],40]
>>> list
[10, 20, ['abc', 'def', 'ghi'], 40]
>>> type(list)
<class 'list'>
>>> list[0]
10
>>> list[2]
['abc', 'def', 'ghi']
>>> list[2][0]
'abc'
>>> list.append([11,22,33])
>>> list
[10, 20, ['abc', 'def', 'ghi'], 40, [11, 22, 33]]
>>> list[4]
[11, 22, 33]
>>> list1=list*2
>>> list1
[10, 20, ['abc', 'def', 'ghi'], 40, [11, 22, 33], 10, 20, ['abc', 'def', 'ghi'], 40, [11, 22, 33]]
>>>

tuple data type:
	>>> t=()
>>> type(t)
<class 'tuple'>
>>> t.append(10)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    t.append(10)
AttributeError: 'tuple' object has no attribute 'append'
>>> t=(10,20,30)
>>> type(t)
<class 'tuple'>
>>> list
<class 'list'>
>>> list=[10,10.25,'python',True]
>>> t=tuple(list)
>>> type(t)
<class 'tuple'>
>>> t
(10, 10.25, 'python', True)
>>> list=[10,20,(10,20),40]
>>> t=tuple(list)
>>> t
(10, 20, (10, 20), 40)
>>> t[0]
10
>>> t[2
  ]
(10, 20)
>>> for i in t:print(i)

10
20
(10, 20)
40
>>> 