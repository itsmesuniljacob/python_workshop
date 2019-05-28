import sys
sys.setrecursionlimit(10000)
def fact(n):
	''' Module to find the factorial of a given number
	recursive limit is set to 10k for this program
	higher factorial may exceed the recursive limit and progam will stop'''
	#print(n)
	return 1 if (n==1) or (n == 0)	else n * fact(n - 1)

# In below way you can use your program as script or a module
if '__main__' == __name__:
	print(fact(5))
else:
	print(__name__)