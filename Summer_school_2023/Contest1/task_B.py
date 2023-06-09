# По заданной строке, являющейся абсолютным адресом в Unix-системе, вам необходимо получить
# канонический адрес.
# В Unix-системе "." соответсвутет текущей директории, ".." — родительской директории, при этом будем считать,
# что любое количество точек подряд, большее двух, соответствует директории с таким названием (состоящем из точек).
# "/" является разделителем вложенных директорий, причем несколько "/" подряд должны интерпретироваться как
# один "/".
# Канонический путь должен обладать следующими свойствами:
# 1) всегда начинаться с одного "/"
# 2) любые две вложенные директории разделяются ровно одним знаком "/"
# 3) путь не заканчивается "/" (за исключением корневой директории, состоящего только из символа "/")
# 4) в каноническом пути есть только директории, т.е. нет ни одного вхождения "." или ".." как соответствия
# текущей или родительской директории
# Формат ввода
# Вводится строка с абсолютным адресом, её длина не превосходит 100.
# Формат вывода
# Выведите канонический путь.
# Пример 1
# Ввод	    Вывод
# /home/      /home
# Пример 2
# Ввод	    Вывод
# /../        /
# Пример 3
# Ввод	       Вывод
# /home//foo/    /home/foo

path = input()
flag = True
path += '/'
while flag:
    if '/./' in path:
        path = path.replace('/./', '/')
    elif '//' in path:
        path = path.replace('//', '/')
    elif '/../' in path:
        pos = path.find('/../')
        if pos == 0:
            path = path[3:]
        else:
            prevpos = path.rfind('/', 0, pos-1)
            path = path[:prevpos] + path[pos+3:]
    else:
        flag = False
if path.endswith('/') and path != '/':
    path = path[:-1]
print(path)