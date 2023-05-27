import os
def file(f):
	with open(f, "rb") as b:
		a = b.read()
	return a

content = file("")