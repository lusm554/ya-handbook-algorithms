money = int(input())
coins_cnt = 0
moneys = list()
while money > 0:
    if money >= 50:
        money -= 50
        moneys.append(50)
    elif money >= 20:
        money -= 20
        moneys.append(20)
    elif money >= 10:
        money -= 10
        moneys.append(10)
    elif money >= 5:
        money -= 5
        moneys.append(5)
    else:
        money -= 1
        moneys.append(1)
print(len(moneys))
print(*moneys)
