n, k, w = map(int, input().split())
order = [list(map(int, input().split())) for _ in range(k)]
order = sorted(order, key = lambda x: -x[0])
result = 0
place = n * w
for i in order:
    if place:
        c, p = i
        amount = min(p, place)
        result += c * amount
        place -= amount
print(result)
