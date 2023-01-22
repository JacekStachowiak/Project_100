import pandas as pd

numbers = [1 , 2 , 3]

new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)
print(new_list)

# 4 linie kodu możemy zapisać w jednej
# new_list = [new_item for item in list]

numbers = [4 , 5 , 6]
new_list = [n for n in numbers]
new_list1 = [n + 1 for n in numbers]
new_list2 = [n * 2 for n in numbers]
new_list3 = [n ** 2 for n in numbers]

print(new_list)
print(new_list1)
print(new_list2)
print(new_list3)

name = 'Angela'
new_list4 = [n for n in name]
print(new_list4)

liczby = [num * 2 for num in range(1 , 6)]
print(liczby)

# warunkowe
# new_list = [new_item for item in list if test]

names = ['Alex', 'Jack', 'Dave', 'Dark', 'Iza']
short_names = [n for n in names if len(n) < 4]
print(short_names)

upper_names = [n.upper() for n in names if len(n) < 4]
print(upper_names)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [num * num for num in numbers]
print(squared_numbers)

result = [n for n in numbers if n % 2 == 0]
print(result)

# zadanie --> pokaż listę w której będą wspólne cyfry z obu plików

with open('file1.txt') as f1:
    file_1 = f1.readlines()
    print(file_1)

with open('file2.txt') as f2:
    file_2 = f2.readlines()
    print(file_2)

result = [int(n1) for n1 in file_1 for n2 in file_2 if n1 == n2]
result2 = [int(num) for num in file_1 if num in file_2]
print(result)
print(result2)

# n2 --> [3, 3, 6, 5, 33, 12, 7]
# n1 --> [3, 3, 6, 5, 33, 12, 7]
# num --> [3, 6, 5, 33, 12, 7]