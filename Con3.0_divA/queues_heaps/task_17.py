# Гоблины Мглистых гор очень любях ходить к своим шаманам. Так как гоблинов много, к шаманам часто образуются очень
# длинные очереди. А поскольку много гоблинов в одном месте быстро образуют шумную толку, которая мешает
# шаманам проводить сложные медицинские манипуляции, последние решили установить некоторые правила касательно
# порядка в очереди.
# Обычные гоблины при посещении шаманов должны вставать в конец очереди. Привилегированные же гоблины,
# знающие особый пароль, встают ровно в ее середину, причем при нечетной длине очереди они встают сразу
# за центром.
# Так как гоблины также широко известны своим непочтительным отношением ко всяческим правилам и законам,
# шаманы попросили вас написать программу, которая бы отслеживала порядок гоблинов в очереди.
# Формат ввода
# В первой строке входных данный записано число N (1≤N≤105) — количество запросов к программе. Следующие N
# строк содержат описание запросов в формате:
# ”+ i” — гоблин с номером i (1≤i≤N) встает в конец очереди.
# ”* i” — привилегированный гоблин с номером i встает в середину очереди.
# ”-” — первый гоблин из очереди уходит к шаманам. Гарантируется, что на момент такого запроса очередь не пуста.
# Формат вывода
# Для каждого запроса типа ”-” программа должна вывести номер гоблина, который должен зайти к шаманам.
# Пример
# Ввод	Вывод
# 7       1
# + 1     2
# + 2     3
# -
# + 3
# + 4
# -
# -


from collections import deque

que_1 = deque()
que_2 = deque()

def insert_base(index):
    que_2.append(index)
    if len(que_2) > len(que_1):
        que_1.append(que_2.popleft())

def insert_prime(index):
    if len(que_1) > len(que_2):
        que_2.appendleft(index)
    else:
        que_1.append(index)

def first():
    res = que_1.popleft()
    if len(que_2) > len(que_1):
        que_1.append(que_2.popleft())
    return res

n = int(input())
for _ in range(n):
    comand_list = input().split()
    comand = comand_list[0]
    if len(comand_list) > 1:
        value = int(comand_list[1])
        if comand == '+':
            insert_base(value)
        elif comand == '*':
            insert_prime(value)
    else:
        print(first())
