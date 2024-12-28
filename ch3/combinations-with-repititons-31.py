"""
Выведите число сочетаний с повторением С(n,k).

Формат ввода
В первой строке находятся два числа n (1≤n≤4), k (1≤k≤4).
"""

n, k = [int(x) for x in input().split(' ')]

def fac(n):
    if n == 0 or n == 1: return 1
    for i in range(1, n):
        n*=i
    return n
res = fac(n + k - 1) // (fac(k) * fac(n - 1))
print(res)


# one more solution
import itertools
print(len(list(itertools.combinations_with_replacement('a'*n, k))))
