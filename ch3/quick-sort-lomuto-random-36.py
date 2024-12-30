import random
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
  return i

def quicksort(lst, low, high):
  if low < high:
    r_i = random.randint(low, high)
    lst[low], lst[r_i] = lst[r_i], lst[low]
    pivot_i = partition(lst, low, high)
    quicksort(lst, low, pivot_i-1)
    quicksort(lst, pivot_i+1, high)

quicksort(lst, 0, cnt-1)
print(' '.join(str(x) for x in lst))
