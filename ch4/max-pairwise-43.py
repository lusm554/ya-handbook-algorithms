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

n = 10
lst = [10] + list(range(1, n))
print(lst)

m1, m2, cnt = max_pairwise(lst)
print(f"{m1=} {m2=} {cnt=} {n*1.5=}")


