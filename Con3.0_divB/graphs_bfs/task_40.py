# Метрополитен состоит из нескольких линий метро. Все станции метро в городе пронумерованы натуральными
# числами от 1 до N. На каждой линии расположено несколько станций. Если одна и та же станция расположена
# сразу на нескольких линиях, то она является станцией пересадки и на этой станции можно пересесть с любой
# линии, которая через нее проходит, на любую другую (опять же проходящую через нее).
# Напишите программу, которая по данному вам описанию метрополитена определит, с каким минимальным числом
# пересадок можно добраться со станции A на станцию B. Если данный метрополитен не соединяет все линии в
# одну систему, то может так получиться, что со станции A на станцию B добраться невозможно, в этом случае
# ваша программа должна это определить.
# Формат ввода
# Сначала вводится число N — количество станций метро в городе (2≤N≤100). Далее следует число M —
# количество линий метро (1≤M≤20). Далее идет описание M линий. Описание каждой линии состоит из числа
# Pi — количество станций на этой линии (2≤Pi≤50) и Pi чисел, задающих номера станций, через которые
# проходит линия (ни через какую станцию линия не проходит дважды).
# Затем вводятся два различных числа: A — номер начальной станции, и B — номер станции, на которую нам
# нужно попасть. При этом если через станцию A проходит несколько линий, то мы можем спуститься на любую
# из них. Так же если через станцию B проходит несколько линий, то нам не важно, по какой линии мы приедем.
# Формат вывода
# Выведите минимальное количество пересадок, которое нам понадобится. Если добраться со станции A на
# станцию B невозможно, программа должна вывести одно число –1 (минус один).
# Пример
# Ввод	    Вывод
# 5           0
# 2
# 4 1 2 3 4
# 2 5 3
# 3 1


from collections import deque

n = int(input())
m = int(input())
lines = [set() for _ in range(m + 1)]
for i in range(1, m + 1):
    p, *s = [int(x) for x in input().split()]
    lines[i] = set(s)

graph = [[] for _ in range(m + 1)]
for i in range(1, m + 1):
    for j in range(i + 1, m + 1):
        if lines[i] & lines[j]:
            graph[i].append(j)
            graph[j].append(i)

stations = [[] for _ in range(n + 1)]
for i in range(1, m + 1):
    for station in lines[i]:
        stations[station].append(i)

visited = [-1] * (m + 1)


def bfs(start):
    deque_ = deque()
    step = 0
    for line in stations[start]:
        visited[line] = step
        deque_.append((line, step))
    while deque_:
        cur_line, cur_step = deque_.popleft()
        step = cur_step + 1
        for neighb in graph[cur_line]:
            if visited[neighb] == -1:
               visited[neighb] = step
               deque_.append((neighb, step))

start, end = map(int, input().split())
bfs(start)
res = visited[stations[end][0]]
for line in stations[end]:
    if visited[line] < res and visited[line] != -1:
        res = visited[line]
print(res)
