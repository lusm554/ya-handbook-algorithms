"""
Задано n отсортированных по неубыванию последовательностей.
Требуется найти отсортированную по неубыванию конкатенацию этих последовательностей.
"""
lst = []
lst_cnt = int(input())
for _ in range(lst_cnt):
  _ = input()
  lst.append([int(x) for x in input().split()])

# too slow
'''
from functools import reduce
def merge(l1, l2):
  merged = []
  while l1 and l2:
    if l1[0] < l2[0]:
      t = l1[0]
      merged.append(t)
      l1.remove(t)
    else:
      t = l2[0]
      merged.append(t)
      l2.remove(t)
  merged += l1
  merged += l2
  return merged
merged = reduce(merge, lst)
'''

# https://www.quora.com/What-is-the-fastest-way-to-merge-k-sorted-arrays-into-one-sorted-array
# O(Nlogk) N is sum of elems cnt, k is cnt of arrays
import heapq
def merge(lst):
  min_heap = []
  merged = []
  # init heap with first elem of lst
  for i in range(lst_cnt):
    heapq.heappush(min_heap, (lst[i][0], i, 0))
  while min_heap:
    val, lst_i, item_i = heapq.heappop(min_heap)
    merged.append(val)
    if item_i+1 < len(lst[lst_i]):
      next_val = lst[lst_i][item_i+1]
      heapq.heappush(min_heap, (next_val, lst_i, item_i+1))
  return merged

merged = merge(lst)
print(' '.join(str(x) for x in merged))
