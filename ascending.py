def sort_asc_number_list(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(1, n-i):
            if numbers[j-1] > numbers[j]:
            # do a tuple swap
                (numbers[j-1], numbers[j]) = (numbers[j], numbers[j-1])
    return numbers

mylist = list(map(int,input('Enter the numbers to be sorted: ').rstrip().split()))
sorted_list = sort_asc_number_list(mylist)
print(sorted_list)

