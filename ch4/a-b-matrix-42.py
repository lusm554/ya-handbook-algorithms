"""
Необходимо вычислить сумму двух матриц C = A+B.
"""
n, m = map(int, input().split())
nmatrix = [
    [*map(int, input().split())]
    for _ in range(n)
]
mmatrix = [
    [*map(int, input().split())]
    for _ in range(n)
]
cmatrix = [
	[i1 + i2 for i1, i2 in zip(r1, r2)]
	for r1, r2 in zip(nmatrix, mmatrix)
]
print('\n'.join(' '.join(str(x) for x in x) for x in cmatrix))
