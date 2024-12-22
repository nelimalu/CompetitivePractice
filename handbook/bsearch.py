values = [1, 2, 5, 9, 10, 11, 12]

def search(arr, l, r, target):
	if r - l <= 1 and target != arr[l]:
		return -1

	mid = (r + l) // 2

	if target == arr[mid]:
		return mid
	if target < arr[mid]:
		return search(arr, l, mid, target)
	return search(arr, mid, r, target)


print(search(values, 0, len(values), 11))
