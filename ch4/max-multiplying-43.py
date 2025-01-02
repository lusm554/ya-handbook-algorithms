n = int(input())
a = [int(x) for x in input().split()]

# simple solution
#res = a.pop(a.index(max(a))) * max(a)
#print(res)

# using heap
import heapq
heap = list()
for i in a:
  heapq.heappush(heap, i)
  if len(heap) > 2: # for less memory use
    heapq.heappop(heap)
m1, m2 = heapq.nlargest(2, heap)
print(m1*m2)
