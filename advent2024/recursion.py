

def pascal(n, k):
	if n == k or k == 0:
		return 1
	return pascal(n - 1, k) + pascal(n - 1, k - 1)


print(pascal(6, 2))
