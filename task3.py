# Напишите программу, которая принимает на вход координаты точки
# (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input('Введите координату Х: '))
y = int(input('Введите координату Y: '))
def checkCoordinats(x,y):
    if x > 0 and y > 0:
        return print('1')
    elif x < 0 and y > 0:
        return print('2') 
    elif x < 0 and y < 0:
        return print('3')
    elif x > 0 and y < 0:
        return print('4') 
    else:
        return print('Введены некорректные данные')
print(f'{x,y} -> ', end = ' ')
checkCoordinats(x,y)