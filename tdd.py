#TDD
import doctest
def average(lst):
	"""
	
	Display average of list of values
	>>> average([10,20,30,40])
	25.0
	>>> average([100,200,300,400])
	250.0
	"""
	tot = 0
	for var in lst:
		tot+=var
	return tot/len(lst)

doctest.testmod()
	