# В строкоремонтную мастерскую принесли строку, состоящую из строчных латинских букв. Заказчик хочет сделать из
# неё палиндром. В мастерской могут за 1 байтландский тугрик заменить произвольную букву в строке любой выбранной
# заказчиком буквой.
# Какую минимальную сумму придётся заплатить заказчику за ремонт строки?

s = input()
res = 0
for i in range(len(s) // 2):
    if s[i] != s[-i - 1]:
        res += 1
print(res)
