money = int(input())
results = list()

for ten in range(money//10+1):
  for five in range(((money-(10*ten))//5)+1):
    one = money - (10 * ten) - (5 * five)
    steps = ten+five+one
    res = f"{steps} {'10 '*ten} {'5 '*five} {'1 '*one}".rstrip()
    results.append(res)

print(len(results))
print('\n'.join(results))
