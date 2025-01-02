n = int(input())
a = [int(x) for x in input().split()]

# simple solution
res = a.pop(a.index(max(a))) * max(a)
print(res)
