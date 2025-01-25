n, S = map(int, input().split())
costs = [int(input()) for _ in range(n)]
costs = sorted(costs, reverse=True)

cnt, s = 0, 0
while s < S:
  s += costs.pop()
  if s <= S:
    cnt += 1
print(cnt)
