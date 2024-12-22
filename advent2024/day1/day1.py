left = []
right = []

with open("input.txt", 'r') as file:
	for line in file.read().splitlines():
		a, b = map(int, line.strip().split())
		left.append(a)
		right.append(b)


def solve1():
	left.sort()
	right.sort()
	total = 0
	for x in range(len(left)):
		total += abs(left[x] - right[x])

	print(total)


def solve2():
	total = 0
	for number in left:
		total += number * right.count(number)
	print(total)


solve2()
