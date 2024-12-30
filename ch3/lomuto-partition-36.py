'''
Постройте разбиение Ломуто относительно первого числа.

Формат ввода
В первой строке задано число n (1≤n≤100000).
Во второй строке задано n.
'''
cnt = int(input())
lst = [int(x) for x in input().split()]

def partition(lst, low, high):
  pivot = lst[low]
  i = low
  for j in range(low+1, high+1):
    if lst[j] <= pivot:
      i+=1
      lst[i], lst[j] = lst[j], lst[i]
  lst[low], lst[i] = lst[i], lst[low]
  return lst

print(' '.join(str(x) for x in partition(lst, 0, cnt-1)))
