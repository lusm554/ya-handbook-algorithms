"""
Головоломка <<Ханойские башни>> состоит из трёх стержней, пронумеруем их слева направо: 1, 2 и 3. Также в головоломке используется стопка дисков с отверстием посередине. Радиус дисков уменьшается снизу вверх. Изначально диски расположены на левом стержне (стержень 1), самый большой диск находится внизу. Диски в игре перемещаются по одному со стержня на стержень. Диск можно надеть на стержень, только если он пустой или верхний диск на нём большего размера, чем перемещаемый. Цель головоломки — перенести все диски со стержня 1 на стержень 3.

Требуется найти последовательность ходов, которая решает головоломку <<Ханойские башни>>.

Формат ввода
В первой строке задано одно число n (3≤n≤10) — количество дисков на первой башне.
"""
def moves_cnt(num_of_bars):
    if num_of_bars == 1:
        return 1
    return 2 * moves_cnt(num_of_bars-1) + 1

def print_moves(n, fromb, tob):
    if n == 1:
        print(fromb, tob)
    else:
        free = 6 - fromb - tob
        print_moves(n-1, fromb, free)
        print(fromb, tob)
        print_moves(n-1, free, tob)

n = int(input())
print(moves_cnt(n))
print_moves(n, 1, 3)

