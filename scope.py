INT = 5
def calc(P, T):
	global INT # you are intending to modify the value of the global variable INT
	print(P * T * INT / 100)
	INT = 6
calc(10000,1)
print(INT)