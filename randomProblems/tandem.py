qtype = int(input())
num_bikes = int(input())
a_citizens = [int(x) for x in input().split()]
b_citizens = [int(x) for x in input().split()]


def solve():
	if qtype == 1:
		a = sorted(a_citizens, reverse=True)
		b = sorted(b_citizens, reverse=True)
	else:
		a = sorted(a_citizens, reverse=True)
		b = sorted(b_citizens)

	total = 0
	for i in range(num_bikes):
		total += max(a[i], b[i])
	return total


print(solve())
