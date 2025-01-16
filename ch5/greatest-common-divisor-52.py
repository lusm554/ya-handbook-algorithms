"""
Для двух чисел a и b найдите их наибольший общий делитель.

Формат ввода
Целые числа a и b (разделённые пробелом).
Ограничения: 1≤a,b≤2⋅10^9
"""
a, b = map(int, input().split())
def gcd(a, b):
    if a <= 0 or b <= 0:
        return max(a, b)
    else:
        return gcd(b, a%b)
print(gcd(a,b))
