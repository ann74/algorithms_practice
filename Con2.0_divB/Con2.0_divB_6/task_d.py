# Фермер Николай нанял двух лесорубов: Дмитрия и Федора, чтобы вырубить лес, на месте
# которого должно быть кукурузное поле. В лесу растут X деревьев.
# Дмитрий срубает по A деревьев в день, но каждый K-й день он отдыхает и не срубает ни одного дерева.
# Таким образом, Дмитрий отдыхает в K-й, 2K-й, 3K-й день, и т.д.
# Федор срубает по B деревьев в день, но каждый M-й день он отдыхает и не срубает ни одного дерева.
# Таким образом, Федор отдыхает в M-й, 2M-й, 3M-й день, и т.д.
# Лесорубы работают параллельно и, таким образом, в дни, когда никто из них не отдыхает,
# они срубают A + B деревьев, в дни, когда отдыхает только Федор — A деревьев, а в дни, когда отдыхает
# только Дмитрий — B деревьев. В дни, когда оба лесоруба отдыхают, ни одно дерево не срубается.
# Фермер Николай хочет понять, за сколько дней лесорубы срубят все деревья, и он сможет засеять
# кукурузное поле.
# Требуется написать программу, которая по заданным целым числам A, K, B, M и X определяет, за
# сколько дней все деревья в лесу будут вырублены.
# Формат ввода
# Входной файл содержит пять целых чисел, разделенных пробелами: A, K, B, M и X
# (1 ≤ A, B ≤ 109 , 2 ≤ K, M ≤ 1018, 1 ≤ X ≤ 1018).
# Формат вывода
# Выходной файл должен содержать одно целое число — искомое количество дней.

def check(days):
    n = (days - days // K) * A + (days - days // M) * B
    return n >= X


def lbinpoisk(l, r):
    while l < r:
        m = (l + r) // 2
        if check(m):
            r = m
        else:
            l = m + 1
    return l

A, K, B, M, X = [int(x) for x in input().split()]
L = 1
R = X
print(lbinpoisk(L, R))
