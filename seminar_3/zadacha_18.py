"""
Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
*Пример:*
5
    1 2 3 4 5
    6
    -> 5
"""    

n = (int(input('Введите количество элементов: ')))
list_A = input("Введите  элементы списка: ").split()
A_num = list(map(int, list_A))
if len(A_num) != n or n == 0:
    print('данные элементы не соответствуют!')
else:
    X = int(input('Введите число X: '))
    min = abs(X - A_num[0])
    index = 0
    for i in range(1, n):
        count = abs(X - A_num[i])
        if count < min:
            min = count
            index = i
    print(f'Число {A_num[index]} наиболее близко по величине к числу {X}')