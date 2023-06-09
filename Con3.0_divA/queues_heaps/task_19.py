# Фирма OISAC выпустила новую версию калькулятора. Этот калькулятор берет с пользователя деньги за совершаемые
# арифметические операции. Стоимость каждой операции в долларах равна 5% от числа, которое является результатом
# операции. На этом калькуляторе требуется вычислить сумму N натуральных чисел (числа известны). Нетрудно
# заметить, что от того, в каком порядке мы будем складывать эти числа, иногда зависит, в какую сумму денег
# нам обойдется вычисление суммы чисел (тем самым оказывается нарушен классический принцип “от перестановки мест
# слагаемых сумма не меняется”).
# Например, пусть нам нужно сложить числа 10, 11, 12 и 13. Тогда если мы сначала сложим 10 и 11 (это обойдется
# нам в 1.05 €), потом результат с 12 (1.65 €), и затем с 13 (2.3 €), то всего мы заплатим 5 €, если же сначала
# отдельно сложить 10 и 11 (1.05 €), потом 12 и 13 (1.25 €) и, наконец, сложить между собой два полученных числа
# (2.3 €), то в итоге мы заплатим лишь 4.6 €. Напишите программу, которая будет определять, за какую минимальную
# сумму денег можно найти сумму данных N чисел.
# Формат ввода
# Первая строка входных данных содержит число N (2 ≤ N ≤ 105). Во второй строке заданы N натуральных чисел,
# каждое из которых не превосходит 10000.
# Формат вывода
# Определите, сколько денег нам потребуется на нахождения суммы этих N чисел. Результат должен быть выведен
# с двумя знаками после десятичной точки.
# Пример 1
# Ввод	Вывод
# 4       4.60
# 10 11 12 13
# Пример 2
# Ввод	Вывод
# 2       0.10
# 1 1


# Используем кучу минимума для чисел и уже сложенных чисел
def push_heap(heap_list, x):
    heap_list.append(x)
    pos = len(heap_list) - 1
    pos_parent = (pos - 1) // 2
    while pos > 0 and heap_list[pos] < heap_list[pos_parent]:
        heap_list[pos], heap_list[pos_parent] = \
            heap_list[pos_parent], heap_list[pos]
        pos = pos_parent
        pos_parent = (pos - 1) // 2


def pop_heap(heap_list):
    ans = heap_list[0]
    heap_list[0] = heap_list[-1]
    pos = 0
    while pos*2 + 2 < len(heap_list):  # т.е. пока есть 2-е детей
        min_son_index = pos*2 + 1
        if heap_list[pos*2 + 2] < heap_list[pos*2 + 1]:
            min_son_index = pos*2 + 2
        if heap_list[pos] > heap_list[min_son_index]:
            heap_list[pos], heap_list[min_son_index] = \
              heap_list[min_son_index], heap_list[pos]
            pos = min_son_index
        else:
            break
    heap_list.pop()
    return ans


n = int(input())
numbers = list(map(int, input().split()))
heap_ = []
answer = 0
for num in numbers:
    push_heap(heap_, num)
while len(heap_) > 1:
    num1 = pop_heap(heap_)
    num2 = pop_heap(heap_)
    res = num1 + num2
    answer += 0.05 * res
    push_heap(heap_, res)
print(f'{answer:.2f}')
