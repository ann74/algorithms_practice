# Вася занимается строительством лесенок из блоков. Лесенка состоит из ступенек, при этом i-ая ступенька
# должна состоять ровно из i блоков.
# По заданному числу блоков n определите максимальное количество ступенек в лесенке, которую можно построить из этих
# блоков.
# Формат ввода
# Ввводится одно число n (1 ≤ n ≤ 231 - 1).
# Формат вывода
# Выведите одно число — количество ступенек в лесенке.

n = int(input())
n_isp, i = 0, 0
while n_isp < n:
    i += 1
    n_isp += i
print(i if n_isp <= n else i - 1)
