# На столе лежали две одинаковые верёвочки целой положительной длины.
# Петя разрезал одну из верёвочек на N частей, каждая из которых имеет целую положительную длину, так что на столе
# стало N+1 верёвочек. Затем в комнату зашла Маша и взяла одну из лежащих на столе верёвочек. По длинам оставшихся
# на столе N верёвочек определите, какую наименьшую длину может иметь верёвочка, взятая Машей.

n = int(input())
l = [int(i) for i in input().split()]
maxl = max(l)
sumother = sum(l) - maxl
if maxl > sumother:
    print(maxl - sumother)
else:
    print(maxl + sumother)