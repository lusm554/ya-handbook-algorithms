n = int(input())
arr = [int(x) for x in input().split()]
arr = sorted(arr)
right = arr[-1] * arr[-2] * arr[-3] * arr[-4]
left = arr[0] * arr[1] * arr[-1] * arr[-2]
full_left = arr[0] * arr[1] * arr[2] * arr[3]
print(max(right, left, full_left))
