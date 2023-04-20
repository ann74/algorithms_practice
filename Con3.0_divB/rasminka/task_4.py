# Контрольная работа
# Петя и Вася — одноклассники и лучшие друзья, поэтому они во всём помогают друг другу. Завтра у них
# контрольная по математике, и учитель подготовил целых K вариантов заданий.
# В классе стоит один ряд парт, за каждой из них (кроме, возможно, последней) на контрольной будут сидеть
# ровно два ученика. Ученики знают, что варианты будут раздаваться строго по порядку: правый относительно
# учителя ученик первой парты получит вариант 1, левый — вариант 2, правый ученик второй парты получит вариант
# 3 (если число вариантов больше двух) и т.д. Так как K может быть меньше чем число учеников N, то после
# варианта K снова выдаётся вариант 1. На последней парте в случае нечётного числа учеников используется
# только место 1.
# Петя самым первым вошёл в класс и сел на своё любимое место. Вася вошёл следом и хочет получить такой же
# вариант, что и Петя, при этом сидя к нему как можно ближе. То есть между ними должно оказаться как можно
# меньше парт, а при наличии двух таких мест с равным расстоянием от Пети Вася сядет позади Пети, а не
# перед ним. Напишите программу, которая подскажет Васе, какой ряд и какое место (справа или слева от учителя)
# ему следует выбрать. Если же один и тот же вариант Вася с Петей писать не смогут, то выдайте одно число  - 1.
# Формат ввода
# В первой строке входных данных находится количество учеников в классе 2 ≤ N ≤ 109.
# Во второй строке — количество подготовленных для контрольной вариантов заданий 2 ≤ K ≤ N.
# В третьей строке — номер ряда, на который уже сел Петя, в четвёртой — цифра 1, если он сел на правое место,
# и 2, если на левое.
# Формат вывода
# Если Вася никак не сможет писать тот же вариант, что и Петя, то выведите  - 1. Если решение существует,
# то выведите два числа — номер ряда, на который следует сесть Васе, и 1, если ему надо сесть на правое место,
# или 2, если на левое. Разрешается использовать только первые N мест в порядке раздачи вариантов.


n = int(input())
k = int(input())
r = int(input())
m = int(input())

number_p = (r - 1) * 2 + m
var_p = (number_p % k == 0) * k + number_p % k
number_v_r = number_p + k
number_v_f = number_p - k
if number_v_r > n and number_v_f < 1:
    print(-1)
elif number_v_f < 1:
    row_v = number_v_r // 2 + number_v_r % 2
    place_v = (number_v_r % 2 == 0) * 2 + number_v_r % 2
    print(row_v, place_v)
elif number_v_r > n:
    row_v = number_v_f // 2 + number_v_f % 2
    place_v = (number_v_f % 2 == 0) * 2 + number_v_r % 2
    print(row_v, place_v)
else:
    row_v_f = number_v_f // 2 + number_v_f % 2
    row_v_r = number_v_r // 2 + number_v_r % 2
    if row_v_r - r <= r - row_v_f:
        row_v = row_v_r
    else:
        row_v = row_v_f
    place_v = (number_v_f % 2 == 0) * 2 + number_v_r % 2
    print(row_v, place_v)