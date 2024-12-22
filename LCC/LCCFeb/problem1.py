from math import sqrt

a, b, n = map(int, input().split())
minimum = min(a, b)
maximum = max(a, b)

nums = []
count = 0

for i in range(int(sqrt(minimum)), 0, -1):
	if count == n:
		break
	if minimum % i == 0 and maximum % i == 0:
		nums.append(i)
		nums.append(int(minimum / i))
		count += 1

print(" ".join([str(x) for x in reversed(sorted(nums, reverse=True)[:n + 1])]))

