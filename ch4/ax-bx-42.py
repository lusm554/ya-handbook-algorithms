"""
Решите немного более сложную задачу.
Необходимо вычислить сумму двух многочленов 
"""
n = int(input())
a = [int(x) for x in input().split()]
m = int(input())
b = [int(x) for x in input().split()]

def sum_poly():
	global n,a,m,b
	max_d = max(n, m)
	a = [0] * (max_d-n) + a
	b = [0] * (max_d-m) + b
	res = [a[i]+b[i] for i in range(max_d+1)]
	while res and res[0] == 0:
		res.pop(0)
	degree = len(res)-1
	return res, degree

res, d = sum_poly()
print(d)
print(' '.join(str(x) for x in res))
