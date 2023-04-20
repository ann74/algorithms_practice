# Правильная скобочная последовательность
# Рассмотрим последовательность, состоящую из круглых, квадратных и фигурных скобок. Программа дожна
# определить, является ли данная скобочная последовательность правильной. Пустая последовательность
# явлется правильной. Если A – правильная, то последовательности (A), [A], {A} – правильные. Если A и B
# – правильные последовательности, то последовательность AB – правильная.
# Формат ввода
# В единственной строке записана скобочная последовательность, содержащая не более 100000 скобок.
# Формат вывода
# Если данная последовательность правильная, то программа должна вывести строку yes, иначе строку no.

s = input()
stack = []
for skob in s:
    if skob in '([{':
        stack.append(skob)
    else:
        if len(stack) == 0:
            print('no')
            break
        elif skob == ')' and stack.pop() != '(':
            print('no')
            break
        elif skob == ']' and stack.pop() != '[':
            print('no')
            break
        elif skob == '}' and stack.pop() != '{':
            print('no')
            break
else:
    if len(stack) == 0:
        print('yes')
    else:
        print('no')
