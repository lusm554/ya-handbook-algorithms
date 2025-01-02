"""
Рассмотрим псевдокод поиска двух максимальных элементов массива:
MaxPairwiseProduct(A[1..n]):
    m1 = A[1]
    m2 = A[2]
    if m2 > m1:
        swap(m1, m2)

    for i from 3 to n:
        if A[i] > m1:
            m2 = m1
            m1 = A[i]
        else:
            if A[i] > m2:
                m2 = A[i]
    return m1 * m2

Определите, можно ли построить такой пример входных данных, чтобы количество сравнений в алгоритме MaxPairwiseProduct было больше 1.5n.

Формат ввода
Целое число n.
Ограничения: 2≤n≤200000.
"""
def max_pairwise(lst):
  m1 = lst[0]
  m2 = lst[1]
  cnt = 0
  cnt += 1
  if m2 > m1:
    m1, m2 = m2, m1
  for i in range(2, len(lst)):
    cnt += 1
    if lst[i] > m1:
      m2 = m1
      m1 = lst[i]
    else:
      cnt += 1
      if lst[i] > m2:
        m2 = lst[i]
  return m1, m2, cnt

def check(n):
  lst = [n] + list(range(1, n))
  m1, m2, comp_cnt = max_pairwise(lst)
  shouldbe = 1.5 * n
  if comp_cnt > shouldbe:
    print('\033[92m', f"{n=} {comp_cnt=} {shouldbe=} {m1=} {m2=}", '\033[0m')
  else:
    print('\033[91m', f"{n=} {comp_cnt=} {shouldbe=} {m1=} {m2=}", '\033[0m')

for n in range(3, 15):
  check(n)

import random
for _ in range(200):
  n = random.randint(3, 200_000)
  check(n)

# solution
n = int(input())
if n > 6:
    print('Yes')
    print(n, ' '.join(str(i) for i in range(1,n)))
else:
    print('No')
