#1 task
main_loop = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = []
even_numbers = []
for index, value in enumerate(main_loop):
    if index % 2 == 0:
        even_numbers.append((index, value))
    else:
        odd_numbers.append((index, value))
print('Even numbers:', even_numbers)
print('Odd numbers:', odd_numbers)

#2 task
num_1 = 2
num_2 = 3
num_3 = 8
num_4 = 4
result = num_1 * num_2
print('Result:', result)
num_2 *= num_1
print('Result:', num_2)
result_2 = num_3 / num_4
print('Result:', result_2)
num_3 /= num_4
print('Result:', num_3)

#3 task
friends = ['John', 'Marta', 'James', 'Artur', 'Kate']
enemies = ['John', 'Johnatan', 'Artur', 'Julia']
for friend in friends:
    if friend == 'James':
        print(f'{friend} is the best friend!')
    elif friend in enemies:
        print(f'{friend} we are not friends anymore.')
    else:
        print(f'{friend} we are the best friends.')

