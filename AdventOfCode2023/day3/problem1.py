with open("../input.txt", 'r') as file:
	schematic = file.read().splitlines()


def is_symbol(char):
	return not char.isnumeric() and char != '.'


def symbol_in_neighbours(x, y):
	for i in range(-1, 2):
		if y - 1 >= 0 and 0 <= x + i < len(schematic[0]) and is_symbol(schematic[y - 1][x + i]):
			return True
		if y + 1 < len(schematic) and 0 <= x + i < len(schematic[0]) and is_symbol(schematic[y + 1][x + i]):
			return True

	if 0 <= x - 1 and is_symbol(schematic[y][x - 1]):
		return True
	if len(schematic[0]) > x + 1 and is_symbol(schematic[y][x + 1]):
		return True

	return False


def main():
	total = 0

	for y, line in enumerate(schematic):
		i = 0
		while i < len(line):
			if schematic[y][i].isnumeric() and symbol_in_neighbours(i, y):

				end = i
				while end < len(schematic[0]):
					if not schematic[y][end].isnumeric():
						break
					end += 1

				start = i
				while start >= 0:
					if not schematic[y][start].isnumeric():
						# start += 1
						break
					start -= 1
				start += 1

				number = schematic[y][start:end]
				# print(y, number)
				total += int(number)
				i = end

			i += 1

	print(total)


main()
