# Легенда
# Вам нужно распилить деревянный брус на несколько кусков в заданных местах. Распилочная компания берет K рублей
# за распил одного бруска длиной K метров на две части.
# Понятно, что различные способы распила приводят к различной суммарной стоимости заказа. Например, рассмотрим
# брус длиной 10 метров, который нужно распилить на расстоянии 2, 4 и 7 м, считая от одного конца. Это можно
# сделать несколькими способами. Можно распилить сначала на отметке 2 м, потом 4 и, наконец, 7 м. Это приведет
# к стоимости 10+8+6=24, потому что сначала длина бруса, который пилили, была 10 м, затем она стала 8 м, и, наконец,
# 6 м. А можно распилить иначе: сначала на отметке 4 м, затем 2, затем 7м. Это приведет к стоимости 10+4+6=20,
# что лучше.
# Определите минимальную стоимость распила бруса на заданные части.
# Формат ввода
# Первая строка входных данных содержит целое число L (2 L  106) — длину бруса и целое число N (1  N  100) —
# количество распилов. Во второй строке записано N целых чисел Сi (0 < Ci < L) в строго возрастающем порядке — места, в которых нужно сделать распилы.
# Формат вывода
# Выведите одно натуральное число — минимальную стоимость распила.
# Пример 1
# Ввод	Вывод
# 10 3    20
# 2 4 7
# Пример 2
# Ввод	  Вывод
# 100 3     200
# 15 50 75
