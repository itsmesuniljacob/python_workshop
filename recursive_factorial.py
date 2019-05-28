#recursive function = a function that can call itself
# OS limit is 1000
# why 1000? if by mistake you write recursive functions more than 1000 , the OS will crash
import sys
sys.setrecursionlimit(10000) # this is to set recursion limit for this program to find factorial more than 1000
def fact(n):
	#print(n)
	return 1 if (n==1) or (n == 0)	else n * fact(n - 1)
num = 1500
print(fact(num))