import math as m

d=2400000
#print(d**d)
try:
	p=m.pow(d,d)
	print(m.exp(p))
except OverflowError:
	p=float('inf')

