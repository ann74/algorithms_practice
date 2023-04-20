# Дан список. Выведите те его элементы, которые встречаются в списке только один раз. Элементы нужно
# выводить в том порядке, в котором они встречаются в списке.
# Формат ввода
# Вводится список чисел. Все числа списка находятся на одной строке.
# Формат вывода
# Выведите ответ на задачу.

a = list(map(int, input().split()))
d = {}
for i in range(len(a)):
    if a[i] not in d:
        d[a[i]] = [0, i]
    d[a[i]][0] += 1
res = []
for k, v in d.items():
    if v[0] == 1:
        res.append((v[1], k))
res.sort()
for item in res:
    print(item[1], end=' ')
