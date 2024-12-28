"""
Задано n интервалов. Требуется найти максимальное количество взаимно непересекающихся интервалов.
Два интервала пересекаются, если они имеют хотя бы одну общую точку.

Формат ввода
В первой строке задано одно число (1≤n≤100) — количество интервалов.
В следующих n строках заданы интервалы li, ri (1 <= li <= ri <= 50).
"""
intervals = []
for _ in range(int(input())):
    intervals.append([*map(int, input().split(' '))])
intervals = sorted(intervals, key=lambda x: x[1])
res = list()
while len(intervals) > 0:
  inter = intervals.pop(0)
  res.append(inter)
  x1, x2 = inter
  intervals = [x for x in intervals if (x2 < x[0]) or (x1 > x[1])]
print(len(res))
