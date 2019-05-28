##
a,b,c,d = 10,20,30,40
def FuncA():
	a,b,c = 100,200,300
	print("In A ",a,b,c,d)
	def FuncB(): # only visible to A
		a,b = 1000, 2000
		print("In B ", a,b,c,d)
		def FuncC(): # only visible to B, not to A
			a = 10000
			print("In C ",a,b,c,d)
		FuncC()
	FuncB()
FuncA()

def FuncA():
	a,b,c = 100,200,300
	print("In A ",a,b,c,d)
	def FuncB(): # only visible to A
		a,b = 1000, 2000
		print("In B ", a,b,c,d)
		def FuncC(): # only visible to B, not to A
			a = 10000
			print("In C ",a,b,c,d)
		FuncC()
	FuncB()
FuncA()

print("In __main__",a,b,c,d)