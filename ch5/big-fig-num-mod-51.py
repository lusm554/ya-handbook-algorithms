"""
Целые числа n и m.

Ограничения: 
n 1≤n≤10^14
m 2≤m≤10^3
"""
n, m = map(int, input().split())

def mul_2x2_mat(A, B, m):
    C = [[0, 0], [0, 0]]
    C[0][0] = (A[0][0]*B[0][0] + A[0][1]*B[1][0]) % m
    C[0][1] = (A[0][0]*B[0][1] + A[0][1]*B[1][1]) % m
    C[1][0] = (A[1][0]*B[0][0] + A[1][1]*B[1][0]) % m
    C[1][1] = (A[1][0]*B[0][1] + A[1][1]*B[1][1]) % m
    return C

def fast_mat_exp(D, n, m):
    if n == 0:
        return [[1, 0], [0, 1]]
    if n % 2 == 0:
        Y = fast_mat_exp(D, n/2, m)
        return mul_2x2_mat(Y, Y, m)
    else:
        Y = fast_mat_exp(D, (n-1)/2, m)
        Y2 = mul_2x2_mat(Y, Y, m)
        return mul_2x2_mat(Y2, D, m)

M = [[0, 1], [1, 1]]
P = fast_mat_exp(M, n, m)
print(P[0][1])
