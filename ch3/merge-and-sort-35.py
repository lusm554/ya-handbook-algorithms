cnt = int(input())
lst = [int(x) for x in input().split()]

def merge(left, right):
	merged = []
	i, j = 0, 0
	while i < len(left) and j < len(right):
		if left[i] <= right[j]:
			merged.append(left[i])
			i+=1
		else:
			merged.append(right[j])
			j+=1
	merged += left[i:]
	merged += right[j:]
	return merged

def mergesort(l):
	if len(l) < 2:
		return l
	mid = len(l)//2
	left, right = l[:mid], l[mid:]
	left, right = mergesort(left), mergesort(right)
	merged = merge(left, right)
	return merged

merged = mergesort(lst)
print(' '.join(str(x) for x in merged))
