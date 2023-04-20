# Вам необходимо построить поле для игры "Сапер" по его конфигурации – размерам и координатам расставленных на нем мин.
# Вкратце напомним правила построения поля для игры "Сапер":
# Поле состоит из клеток с минами и пустых клеток
# Клетки с миной обозначаются символом *
# Пустые клетки содержат число ki,j, 0≤ ki, j ≤ 8 – количество мин на соседних клетках. Соседними клетками являются
# восемь клеток, имеющих смежный угол или сторону.

m, n, k = (int(x) for x in input().split())
pole = [[0] * n for _ in range(m)]
for _ in range(k):
    x, y = (int(i) for i in input().split())
    pole[x - 1][y - 1] = '*'
indexes = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
for i in range(m):
    for j in range(n):
        if pole[i][j] != '*':
           number = sum([pole[i + x][j + y] == '*' for x, y in indexes if 0 <= i + x < m and 0 <= j + y < n])
           pole[i][j] = number
for line in pole:
    print(*line)