# По данному числу N определите количество последовательностей из нулей и единиц длины N, в которых никакие
# три единицы не стоят рядом.
# Формат ввода
# Во входном файле написано натуральное число N, не превосходящее 35.
# Формат вывода
# Выведите количество искомых последовательностей. Гарантируется, что ответ не превосходит 231-1.
# Пример
# Ввод	Вывод
# 1       2


n = int(input())
dp = [0] * max((n + 1), 4)
dp[1] = 2
dp[2] = 4
dp[3] = 7
for i in range(4, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
print(dp[n])