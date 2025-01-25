n = int(input())
prices = sorted(map(int, input().split()))
clicks = sorted(map(int, input().split()))
s = 0
for p, c in zip(prices, clicks):
    s += p*c
print(s)
