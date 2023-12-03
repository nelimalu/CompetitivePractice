with open("../input.txt", 'r') as file:
	schematic = file.read().splitlines()


def is_symbol(char):
	return char.isnumeric()


def find_digits(x, y):
	digit_locations = [
		list("..."),
		list("..."),
		list("...")
	]


	for i in range(-1, 2):
		if y - 1 >= 0 and 0 <= x + i < len(schematic[0]) and is_symbol(schematic[y - 1][x + i]):
			digit_locations[0][i + 1] = 'X'
		if y + 1 < len(schematic) and 0 <= x + i < len(schematic[0]) and is_symbol(schematic[y + 1][x + i]):
			digit_locations[2][i + 1] = 'X'

	if 0 <= x - 1 and is_symbol(schematic[y][x - 1]):
		digit_locations[1][0] = 'X'
	if len(schematic[0]) > x + 1 and is_symbol(schematic[y][x + 1]):
		digit_locations[1][2] = 'X'


	digit_locs = []
	num_numbers = 0
	for i in [0, 2]:
		if "".join(digit_locations[i]) == 'XXX':
			digit_locs.append((y + (i - 1), x))
		elif "".join(digit_locations[i]) == 'X.X':
			digit_locs.append((y + (i - 1), x - 1))
			digit_locs.append((y + (i - 1), x + 1))
		elif "".join(digit_locations[i]) != '...':
			digit_locs.append((y + (i - 1), x + digit_locations[i].index('X') - 1))

	if digit_locations[1][0] == 'X':
		digit_locs.append((y, x - 1))
	if digit_locations[1][2] == 'X':
		digit_locs.append((y, x + 1))

	if len(digit_locs) == 2:
		return digit_locs

	return False


def main():
	total = 0

	for _y, line in enumerate(schematic):
		for _x, char in enumerate(line):
			if char == '*':
				locations = find_digits(_x, _y)
				if locations:
					values = []
					for number_location in locations:
						y, x = number_location

						end = x
						while end < len(schematic[0]):
							if not schematic[y][end].isnumeric():
								break
							end += 1

						start = x
						while start >= 0:
							if not schematic[y][start].isnumeric():
								break
							start -= 1
						start += 1

						number = schematic[y][start:end]
						values.append(int(number))
					total += values[0] * values[1]

	print(total)


main()
