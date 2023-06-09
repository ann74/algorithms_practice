# Из шахматной доски по границам клеток выпилили связную (не распадающуюся на части) фигуру без дыр.
# Требуется определить ее периметр.
# Формат ввода
# Сначала вводится число N (1 ≤ N ≤ 64) – количество выпиленных клеток. В следующих N строках вводятся координаты
# выпиленных клеток, разделенные пробелом (номер строки и столбца – числа от 1 до 8). Каждая выпиленная клетка
# указывается один раз.
# Формат вывода
# Выведите одно число – периметр выпиленной фигуры (сторона клетки равна единице).

n = int(input())
pole = [[0] * 10 for _ in range(10)]
for _ in range(n):
    x, y = (int(i) for i in input().split())
    pole[x][y] = 1
ans = 0
sosedi = [(-1, 0), (0, 1), (1, 0), (0, -1)]
for i in range(1, 9):
    for j in range(1, 9):
        if pole[i][j] == 1:
            ans += sum([pole[i + x][j + y] == 0 for x, y in sosedi])
print(ans)
