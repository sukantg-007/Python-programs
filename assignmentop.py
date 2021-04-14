>>> a=10
>>> c,b,a=10,a+10,a+20
>>> c
10
>>> b
20
>>> a
30
>>> a=10
>>> c,a,b=10,a+10,a+20
>>> c
10
>>> b
30
>>> a=10
>>> a+=10#a=a+10
>>> a
20
>>> a-=5
>>> a
15
>>> a*=2
>>> a
30
>>> a/=10
>>> a
3.0
>>> a%=2
>>> a
1.0
>>> 5/2
2.5
>>> 5//2
2
>>> a
1.0
>>> a//=2
>>> a
0.0
>>> a+=10
>>> a
10.0
>>> a**=2#a=a**2
>>> a
100.0
>>> a=int(a)
>>> a
100
>>> a/1
100.0
>>> floor(a)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    floor(a)
NameError: name 'floor' is not defined
>>> import math as m
>>> m.floor(a)
100
>>> 


Equality operator:
	>>> True < True
False
>>> False < True
True
>>> a,b=10,20
>>> a<b
True
>>> a>b
False
>>> a<=b
True
>>> a>=b
False
>>> 'abc'<'def'
True
>>> 'abc'>'def'
False
>>> 'abc'<'abd'
True
>>> 'a'<97
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    'a'<97
TypeError: '<' not supported between instances of 'str' and 'int'
>>> 'a'==97
False
>>> a=10,b=20
SyntaxError: cannot assign to literal
>>> a=10
>>> b=10
>>> a==b
True
>>> a is b
True
>>> id(a)
2579434924624
>>> id(b)
2579434924624
>>> a!=b
False
>>> 

logical operator:
	>>> 
>>> 
>>> True and True
True
>>> True and False
False
>>> 10 and 10
10
>>> 10 and 20
20
>>> 0 and 10
0
>>> 'python' and 10
10
>>> 'python' and ''
''
>>> 10 or 20
10
>>> '' or 10
10
>>> 0 or 10
10
>>> 'python' or ''
'python'
>>> a=10
>>> not a
False
>>> not ''
True
>>> not 0
True
>>> 