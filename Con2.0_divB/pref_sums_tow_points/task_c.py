# В новом учебном году на занятия в компьютерные классы Дворца Творчества Юных пришли учащиеся, которые
# были разбиты на N групп. В i-й группе оказалось Xi человек. Тут же перед директором встала серьезная
# проблема: как распределить группы по аудиториям. Во дворце имеется M ≥ N аудиторий, в j-й аудитории
# имеется Yj компьютеров. Для занятий необходимо, чтобы у каждого учащегося был компьютер и еще один
# компьютер был у преподавателя. Переносить компьютеры из одной аудитории в другую запрещается.
# Помогите директору!
# Напишите программу, которая найдет, какое максимальное количество групп удастся одновременно
# распределить по аудиториям, чтобы всем учащимся в каждой группе хватило компьютеров, и при этом
# остался бы еще хотя бы один для учителя.
# Формат ввода
# На первой строке входного файла расположены числа N и M (1 ≤ N ≤ M ≤ 1000). На второй строке
# расположено N чисел — X1, …, XN (1 ≤ Xi ≤ 1000 для всех 1 ≤ i ≤ N). На третьей строке расположено
# M чисел Y1, ..., YM (1 ≤ Yi ≤ 1000 для всех 1 ≤ i ≤ M).
# Формат вывода
# Выведите на первой строке число P - количество групп, которые удастся распределить по аудиториям.
# На второй строке выведите распределение групп по аудиториям – N чисел, i-е число должно
# соответствовать номеру аудитории, в которой должна заниматься i-я группа. (Нумерация как групп,
# так и аудиторий, начинается с 1). Если i-я группа осталась без аудитории, i-е число должно быть
# равно 0. Если допустимых распределений несколько, выведите любое из них.

def readandenum():
    x = [int(i) for i in input().split()]
    for i in range(len(x)):
        x[i] = (x[i], i + 1)
    x.sort()
    return x

n, m = (int(x) for x in input().split())
x = readandenum()
y = readandenum()
ynum = 0
res = 0
ans = [0] * (n + 1)
for pup, xnum in x:
    while ynum < m and y[ynum][0] < pup + 1:
        ynum += 1
    if ynum == m:
        break
    ans[xnum] = y[ynum][1]
    ynum += 1
    res += 1
print(res)
print(*ans[1:])

