# Минимальный прямоугольник
# На клетчатой плоскости закрашено K клеток. Требуется найти минимальный по площади прямоугольник, со сторонами,
# параллельными линиям сетки, покрывающий все закрашенные клетки.
# Формат ввода
# Во входном файле, на первой строке, находится число K (1 ≤ K ≤ 100). На следующих K строках находятся пары
# чисел Xi и Yi – координаты закрашенных клеток (|Xi|, |Yi| ≤ 109).
# Формат вывода
# Выведите в выходной файл координаты левого нижнего и правого верхнего углов прямоугольника.


k = int(input())
x = []
y = []
for _ in range(k):
    i, j = map(int, input().split())
    x.append(i)
    y.append(j)
print(min(x), min(y), max(x), max(y))
