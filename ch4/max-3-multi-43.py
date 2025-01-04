"""
Дана последовательность целых чисел.
"""
n = int(input())
a = [int(x) for x in input().split()]

def max_triple_mul(lst):
    lst = sorted(lst)
    return max(lst[-1]*lst[-2]*lst[-3], lst[0]*lst[1]*lst[-1])
print(max_triple_mul(a))
