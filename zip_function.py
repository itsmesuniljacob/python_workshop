numbers = [1, 2, 3, 4, 5]
letters = ['a', 'b', 'c', 'd', 'e']
for num,alpha in zip(numbers,letters):
    print('{} number is related to {}'.format(num,alpha))