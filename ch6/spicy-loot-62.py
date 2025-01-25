n, W = map(int, input().split())
w = [tuple(map(int, input().split())) for _ in range(n)]
w = sorted(w, key=lambda x: x[0]/x[1])
#print(w)

'''
def max_loot(W, w):
  if W == 0 or len(w) == 0:
    return 0 
  cost, weight = w.pop()
  amount = min(weight, W)
  value = cost / weight * amount
  return value + max_loot(W-amount, w)

print(max_loot(W, w))
'''
vsum = 0
while 1:
  if W == 0 or len(w) == 0:
    break
  cost, weight = w.pop()
  amount = min(weight, W)
  value = cost / weight * amount
  vsum += value
  W -= amount
print(vsum)
