'''
Выведите число перестановок P(n).

Формат ввода
В первой строке находится одно число n (1≤n≤7).
'''

a = int(input())
for i in range(1, a):
    a *= i
print(a)