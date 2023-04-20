# Сумма в прямоугольнике
# Вам необходимо ответить на запросы узнать сумму всех элементов числовой матрицы N×M в прямоугольнике с
# левым верхним углом (x1, y1) и правым нижним (x2, y2)
# Формат ввода
# В первой строке находится числа N, M размеры матрицы (1 ≤ N, M ≤ 1000) и K — количество запросов (1 ≤ K ≤ 100000).
# Каждая из следующих N строк содержит по M чисел`— элементы соответствующей строки матрицы (по модулю
# не превосходят 1000). Последующие K строк содержат по 4 целых числа, разделенных пробелом x1 y1 x2 y2
# — запрос на сумму элементов матрице в прямоугольнике (1 ≤ x1 ≤ x2 ≤ N, 1 ≤ y1 ≤ y2 ≤ M)
# Формат вывода
# Для каждого запроса на отдельной строке выведите его результат — сумму всех чисел в элементов матрице в
# прямоугольнике (x1, y1), (x2, y2)


n, m, k = map(int, input().split())
a = []
for _ in range(n):
    row = [int(x) for x in input().split()]
    a.append(row)
a_pref = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        a_pref[i][j] = a_pref[i][j - 1] + a_pref[i - 1][j] - a_pref[i - 1][j - 1] + a[i - 1][j - 1]
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    res = a_pref[x2][y2] - a_pref[x2][y1-1] - a_pref[x1-1][y2] + a_pref[x1-1][y1-1]
    print(res)
