with open("input.txt", 'r') as file:
	data = [[int(n) for n in line.split()] for line in file.read().splitlines()]


def solve1():
	safe = 0
	for line in data:
		increasing = line[0] < line[1]
		print(increasing)
		current = 0
		for x, value in enumerate(line[1:]):
			if 1 <= abs(value - line[x]) <= 3 and line[x] < value == increasing:
				current = 1
			else:
				break
		else:
			current = 0
		safe += current
	print(safe)


solve1()
