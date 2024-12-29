# selection sort
cnt = int(input())
lst = [int(x) for x in input().split()]
for i in range(cnt):
  for j in range(i):
    if lst[i] < lst[j]:
      lst[i], lst[j] = lst[j], lst[i]
print(' '.join(str(x) for x in lst))
