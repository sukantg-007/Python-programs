class A:
	def m1(self):
		print('A-m1-method')

class B:
	def m1(self):
		print('B-m1-method')

class C(B,A):
	pass

c=C()

c.m1()