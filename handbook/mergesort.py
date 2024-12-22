values = [int(n) for n in input().split()]


def merge(arr1, arr2):
	merged = []
	c1 = 0
	c2 = 0
	for i in range(len(arr1) + len(arr2)):
		if c1 == len(arr1):
			return merged + arr2[c2:]
		elif c2 == len(arr2):
			return merged + arr1[c1:]
		elif arr1[c1] > arr2[c2]:
			merged.append(arr1[c1])
			c1 += 1
		else:
			merged.append(arr2[c2])
			c2 += 1
	return merged


def mergesort(arr):
	if len(arr) == 1:
		return arr
	mid = len(arr) // 2
	return merge(mergesort(arr[:mid]), mergesort(arr[mid:]))


print(mergesort(values))
