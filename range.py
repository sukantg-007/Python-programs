range data type:

>>> r=range(10)
>>> type(r)
<class 'range'>
>>> r
range(0, 10)
>>> for i in r:print(i)

0
1
2
3
4
5
6
7
8
9
>>> r[0]
0
>>> r[1]
1
>>> r[1:4]
range(1, 4)
>>> r[1]=10
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    r[1]=10
TypeError: 'range' object does not support item assignment
>>> r=range(10,30)
>>> r
range(10, 30)
>>> for i in r:print(i)

10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
>>> r=range(10,30,2)
>>> r
range(10, 30, 2)
>>> for i in r:print(i)

10
12
14
16
18
20
22
24
26
28
>>> r=range(10,30,3)
>>> for i in r:print(i)

10
13
16
19
22
25
28
>>> r=range(10)
>>> r[1::2]
range(1, 10, 2)
>>> for i in r[1::2]:print(i)

1
3
5
7
9
>>> r=range(10.5,20.5)


>>> r=range(10.5,20.5)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    r=range(10.5,20.5)
TypeError: 'float' object cannot be interpreted as an integer
>>> r=range(-5,-1)
>>> for i in r:print(i)

-5
-4
-3
-2
>>> r=range(-1,-5)
>>> r
range(-1, -5)
>>> for i in r:print(i)

>>> list=[10,20,10,30]
>>> s=set(list)
>>> s
{10, 20, 30}
>>> list=['python','java','c']
>>> list
['python', 'java', 'c']
>>> s=set(list)
>>> s
{'java', 'c', 'python'}
>>> list=[1,2,3,4,5]
>>> s=set(list)
>>> s
{1, 2, 3, 4, 5}
>>> s.add('python')
>>> s
{1, 2, 3, 4, 5, 'python'}
>>> s.add('java')
>>> s
{1, 2, 3, 4, 5, 'python', 'java'}
>>> s.remove(4)
>>> s
{1, 2, 3, 5, 'python', 'java'}
>>> list=[10,20,10,30]
>>> fs=frozenset(list)
>>> fs
frozenset({10, 20, 30})
>>> fs.add(40)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    fs.add(40)
AttributeError: 'frozenset' object has no attribute 'add'
>>> fs.remove(10)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    fs.remove(10)
AttributeError: 'frozenset' object has no attribute 'remove'


dictionary data type:
