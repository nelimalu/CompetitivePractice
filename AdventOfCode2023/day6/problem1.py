import math

with open("../input.txt", 'r') as file:
	times, distances = [[int(y) for y in x.split(": ")[1].strip().split()] for x in file.read().splitlines()]


def ceiling(number):
	return int(number) + 1



def floor(number):
	frac = number - int(number)
	if frac == 0:
		return int(number) - 1
	else:
		return math.floor(number)



product = 1
for x, time in enumerate(times):
	discriminant = math.sqrt(time ** 2 + 4 * -distances[x])
	a = (-time + discriminant) / -2
	b = (-time - discriminant) / -2
	left = ceiling(min(a, b))
	right = floor(max(a, b))

	# print(f"RACE {x + 1}:")
	# print(f"	raw: {a}, {b}")
	# print(f"	rounded: {left}, {right}")
	# print(f"distance {right - left + 1}")
	product *= right - left + 1


print(product)
