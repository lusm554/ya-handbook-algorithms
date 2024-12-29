#n = int(input())
n = 3
cnt = 0

def ht(disk, frombar, tobar):
	if disk == 1:
		return
	#unusedbar = (disk+frombar+tobar) - frombar - tobar
	unusedbar = 6 - frombar - tobar
	print(f"{disk=} {frombar=} {tobar=} {unusedbar=}")
	ht(disk-1, frombar, unusedbar)
	ht(disk-1, unusedbar, tobar)

ht(disk=n, frombar=1, tobar=3)

'''
 HanoiTowers(n,fromPeg,toPeg)
    if n = 1:
        output “Move disk from peg fromPeg to peg toPeg”
        return
    unusedPeg = 6 - fromPeg - toPeg
    HanoiTowers(n−1,fromPeg,unusedPeg)
    output “Move disk from peg fromPeg to peg toPeg”
    HanoiTowers(n−1,unusedPeg,toPeg)

1. Сначала нужно переместить n-1 дисков на стержень посередине 2
2. Самый большой диск n переместить на 3 стержень
3. Переместить диски со стержня посередине 2 на 3 стержень
'''



