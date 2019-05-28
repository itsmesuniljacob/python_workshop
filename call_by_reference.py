# no return in the function, call by reference
# with dictionaries and list you can implement call by reference
l = [10,20]
def swap(list):
	list[0],list[1] = list[1],list[0]
swap(l)
print(l)