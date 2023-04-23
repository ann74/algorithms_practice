# Дана текстовая строка. С ней можно выполнять следующие операции:
# 1. Заменить один символ строки на другой символ.
# 2. Удалить один произвольный символ.
# 3. Вставить произвольный символ в произвольное место строки.
# Например, при помощи первой операции из строки «СОК» можно получить строку «СУК», при помощи второй операци
# — строку «ОК», при помощи третьей операции — строку «СТОК».
# Минимальное количество таких операций, при помощи которых можно из одной строки получить другую, называется
# стоимостью редактирования или расстоянием Левенштейна.
# Определите расстояние Левенштейна для двух данных строк.
# Формат ввода
# Программа получает на вход две строки, длина каждой из которых не превосходит 1000 символов, строки состоят
# только из заглавных латинских букв.
# Формат вывода
# Требуется вывести одно число — расстояние Левенштейна для данных строк.
# Пример
# Ввод	    Вывод
# ABCDEFGH    3
# ACDEXGIH


s1 = input()
s2 = input()
n = len(s1)
m = len(s2)

table = [[0] * (m + 1) for _ in range(n + 1)]
for j in range(1, m + 1):
    table[0][j] = j
for i in range(1, n + 1):
    table[i][0] = i
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if s1[i - 1] == s2[j - 1]:
            table[i][j] = table[i - 1][j - 1]
        else:
            table[i][j] = min(table[i][j - 1], table[i - 1][j], table[i - 1][j - 1]) + 1

print(table[n][m])
