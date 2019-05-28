def total(*numbers):
	result = 0
	for number in numbers:
		result += number
	return result
print(total(10,20,30,4,5,6,7,7,8,9,9,1))