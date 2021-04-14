1. function int():-
		>>> int(12.2)
		12

		>>> int("10")
		10
		>>> int("10")
		10
		>>> type("10")
		<class 'str'>
		>>> int("10")
		10
		>>> int("a10")
		Traceback (most recent call last):
		  File "<pyshell#9>", line 1, in <module>
			int("a10")
		ValueError: invalid literal for int() with base 10: 'a10'
		>>> int(10+2j)
		Traceback (most recent call last):
		  File "<pyshell#10>", line 1, in <module>
			int(10+2j)
		TypeError: can't convert complex to int
		>>> int(True)
		1
		>>> int(False)
		0
		>>> int("10.25")
		Traceback (most recent call last):
		  File "<pyshell#13>", line 1, in <module>
			int("10.25")
		ValueError: invalid literal for int() with base 10: '10.25'

2. Function float():-
		>>> float()
		0.0

		>>> float()
		0.0
		>>> float(10)
		10.0
		>>> float("10.25")
		10.25
		>>> float("a10.25")
		Traceback (most recent call last):
		  File "<pyshell#3>", line 1, in <module>
			float("a10.25")
		ValueError: could not convert string to float: 'a10.25'
		>>> float(10+2j)
		Traceback (most recent call last):
		  File "<pyshell#4>", line 1, in <module>
			float(10+2j)
		TypeError: can't convert complex to float
		>>> float(True)
		1.0

3. Function complex():-

		>>> complex()
		0j

		>>> complex(10)
		(10+0j)
		>>> complex("10")
		(10+0j)
		>>> complex(10.25)
		(10.25+0j)
		>>> complex("a10")
		Traceback (most recent call last):
		  File "<pyshell#11>", line 1, in <module>
			complex("a10")
		ValueError: complex() arg is a malformed string
		>>> complex(True)
		(1+0j)
		>>> complex(10,20)
		(10+20j)
		>>> complex(10.25,10.25)
		(10.25+10.25j)
		>>> complex(True,False)
		(1+0j)
		>>> complex(True,True,True)
		Traceback (most recent call last):
		  File "<pyshell#16>", line 1, in <module>
			complex(True,True,True)
		TypeError: complex() takes at most 2 arguments (3 given)


4. function str():-
		''
		>>> str("10")
		'10'
		>>> str(10.25)
		'10.25'
		>>> str(True)
		'True'
		>>> str(10+2j)
		'(10+2j)'

5. function bool():-

		>>> bool(10)
		True
		>>> bool(0)
		False
		>>> bool(9)
		True
		>>> bool(10.25)
		True
		>>> bool(0.0)
		False
		>>> bool("abc")
		True
		>>> bool("")
		False
		>>> bool(" ")
		True
		>>> bool("     ")
		True
		>>> bool(<)
		SyntaxError: invalid syntax
		>>> bool("<")
		True
