# Во входной строке записана последовательность чисел через пробел. Для каждого числа выведите слово YES
# (в отдельной строке), если это число ранее встречалось в последовательности или NO, если не встречалось.
# Формат ввода
# Вводится список чисел. Все числа списка находятся на одной строке.
# Формат вывода
# Выведите ответ на задачу.

a = list(map(int, input().split()))
b = set()
for num in a:
    if num in b:
        print('YES')
    else:
        print('NO')
        b.add(num)
