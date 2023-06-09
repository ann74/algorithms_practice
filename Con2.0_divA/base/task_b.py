# В первой строке входного файла записано целое число N (1 ≤ N ≤ 10) - количество заданных Петей вопросов.
# Каждая из N последующих строк содержит описание четырех точек - четыре пары целых чисел X и Y
# (−100 ≤ X ≤ 100, −100 ≤ Y ≤ 100), обозначающих координаты точки. Гарантируется, что четыре точки, о которых
# идет речь в одном вопросе, не лежат на одной прямой.
# Формат вывода
# Для каждого из вопросов выведите "YES", если четыре заданные точки могут образовать параллелограмм,
# и "NO" в противном случае. Ответ на каждый из запросов должен быть в отдельной строке без кавычек.

def par(a1, b1, a2, b2):
    if a1[0] == b1[0]:
        k1 = 999.9
    else:
        k1 = (a1[1] - b1[1]) / (a1[0] - b1[0])
    if a2[0] == b2[0]:
        k2 = 999.9
    else:
        k2 = (a2[1] - b2[1]) / (a2[0] - b2[0])
    if abs(k1 - k2) < 0.001:
        return True
    return False

n = int(input())
indexes = ((0, 1, 2, 3), (1, 2, 3, 0), (0, 2, 1, 3))
for _ in range(n):
    a = [int(x) for x in input().split()]
    points = [(a[i], a[i+1]) for i in range(0, 8, 2)]
    npar = 0
    for index in indexes:
        a, b, c, d = points[index[0]], points[index[1]], points[index[2]], points[index[3]]
        dist1 = (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
        dist2 = (c[0] - d[0]) ** 2 + (c[1] - d[1]) ** 2
        if dist1 == dist2 and par(a, b, c, d):
            npar += 1
    if npar >= 2:
        print('YES')
    else:
        print('NO')

