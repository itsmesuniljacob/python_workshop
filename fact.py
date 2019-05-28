import sys
sys.setrecursionlimit(10000)
def fact(n):
	''' Module to find the factorial of a given number
	recursive limit is set to 10k for this program
	higher factorial may exceed the recursive limit and progam will stop'''
	#print(n)
	return 1 if (n==1) or (n == 0)	else n * fact(n - 1)

def fact1(n):
	return 1 if (n==1) or (n == 0)	else n * fact1(n - 1)