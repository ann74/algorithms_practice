# В левом верхнем углу прямоугольной таблицы размером N×M
#  находится черепашка. В каждой клетке таблицы записано некоторое число. Черепашка может перемещаться вправо
# или вниз, при этом маршрут черепашки заканчивается в правом нижнем углу таблицы.
# Подсчитаем сумму чисел, записанных в клетках, через которую проползла черепашка (включая начальную и
# конечную клетку). Найдите наибольшее возможное значение этой суммы и маршрут, на котором достигается эта
# сумма.
# Формат ввода
# В первой строке входных данных записаны два натуральных числа N и M, не превосходящих 100 — размеры таблицы.
# Далее идет N строк, каждая из которых содержит M чисел, разделенных пробелами — описание таблицы. Все числа
# в клетках таблицы целые и могут принимать значения от 0 до 100.
# Формат вывода
# Первая строка выходных данных содержит максимальную возможную сумму, вторая — маршрут, на котором достигается
# эта сумма. Маршрут выводится в виде последовательности, которая должна содержать N-1 букву D, означающую
# передвижение вниз и M-1 букву R, означающую передвижение направо. Если таких последовательностей несколько,
# необходимо вывести ровно одну (любую) из них.
# Пример
# Ввод	        Вывод
# 5 5             74
# 9 9 9 9 9       D D R R R R D D
# 3 0 0 0 0
# 9 9 9 9 9
# 6 6 6 6 8
# 9 9 9 9 9


n, m = map(int, input().split())
table = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    row = [int(x) for x in input().split()]
    for j in range(1, m + 1):
        table[i][j] = max(table[i][j - 1], table[i - 1][j]) + row[j - 1]
print(table[-1][-1])
res = []
while m > 1 or n > 1:
    temp_d = {table[n][m - 1]: ('R', 0, -1), table[n - 1][m]: ('D', -1, 0)}
    temp = temp_d[max(temp_d)]
    res.append(temp[0])
    n += temp[1]
    m += temp[2]
print(*res[::-1])