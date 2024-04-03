numbers = [1, -5, 0, 10, 100, 67, 55, 20, 34]

new_list = []

for num in numbers:
    if num % 2 == 0:
        new_list.append(num)

new_list_2 = [num for num in numbers if num % 2 == 0]

names = ['ssy', 'syy', 'sy', 'haha', 'luke']

filtered_name = []

for name in names:
    if name.startswith('s'):
        filtered_name.append(name)


f_n = [name for name in names if name.startswith('s')]
print(f_n)