# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. Последняя строка содержит число X
# Ввод элементов: 5
# Введенные элементы: 1 2 3 4 5 (записываются в список)
# Вводим число: 3
# Вводится количество повторений этой цифры: -> 1

N = int (input('Здравствуйте! Введите количество элементов: ')) 
list_0 = []
СoincidenceNum = 0
for i in range(N):
    list_0.append(int(input(f"Введите число №{i+1}: ")))
X = int (input('Введите элемент для проверки совпадений: '))
for i in range(len(list_0)):
    if list_0[i] == X:
        СoincidenceNum +=1
print(f"Количество совпадений = {СoincidenceNum}")
