5# В атриуме нового корпуса ФНК урбанисты установили модные гранитные лавочки (на которых холодно сидеть зимой
# и жарко летом). Лавочка устроена следующим образом: несколько одинаковых кубических гранитных блоков ставятся
# в ряд, а на них кладется гранитная плита.
# При этом блоки располагаются так, чтобы плита не падала: для этого достаточно, чтобы и слева, и справа от центра
# плиты был хотя бы один гранитный блок или его часть (в частности, если центр плиты приходится на середину
# какого-нибудь блока, то и слева, и справа от центра плиты находится часть блока, и плита не падает).
# На ФНК много певокурсников (но это только пока не произошли отчисления за списывания на курсе ОиМП) и им
# не хватает стульев в аудиториях. Студенты обнаружили, что блоки можно использовать в аудитории в качестве сиденья.
# Можно по одному вытаскивать блоки, находящиеся с краю (как слева, так и справа). Они хотят вытащить из-под лавочки
# как можно больше блоков так, чтобы она при этом не упала (передвигать оставшиеся блоки нельзя). Определите,
# какие блоки они должны оставить.

l, n = (int(x) for x in input().split())
blocks = [0] * l
for x in input().split():
    blocks[int(x)] = 1
a, b = (l - 1) // 2, l // 2
res = set()
while blocks[a] == 0 and a > -1:
    a -= 1
res.add(a)
while blocks[b] == 0 and b < l + 1:
    b += 1
res.add(b)
print(*sorted(res))
