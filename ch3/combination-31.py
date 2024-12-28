"""
Выведите число сочетаний C(n,k).

Формат ввода:
В первой строке находится два числа n (1≤n≤7), k (1≤k≤7).

Notes:
В формуле n! / (k! (n - k)!), если сократить, то получится (n-k+1)(n-k+2)..n/k!
"""
n, k = [int(x) for x in input().split(' ')]
if k <= n:
    nn, kk = 1, 1
    for i in range(1, min(k, n-k) + 1):
        nn *= n
        kk *= i
        n -= 1
    print(nn//kk)
else:
    print(0)
