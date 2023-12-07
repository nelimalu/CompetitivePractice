import math

with open("../input.txt", 'r') as file:
	time, distance = [int("".join(x.split(": ")[1].strip().split())) for x in file.read().splitlines()]


def ceiling(number):
	return int(number) + 1



def floor(number):
	frac = number - int(number)
	if frac == 0:
		return int(number) - 1
	else:
		return math.floor(number)



discriminant = math.sqrt(time ** 2 + 4 * -distance)
a = (-time + discriminant) / -2
b = (-time - discriminant) / -2
left = ceiling(min(a, b))
right = floor(max(a, b))

product = right - left + 1
print(product)
