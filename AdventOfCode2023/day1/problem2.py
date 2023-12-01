with open('../input.txt', 'r') as file:
	data = file.read().splitlines()


total = 0
for line in data:
	parsed = line.replace('one', 'o1e')
	parsed = parsed.replace('two', 't2o')
	parsed = parsed.replace('three', 't3e')
	parsed = parsed.replace('four', 'f4r')
	parsed = parsed.replace('five', 'f5e')
	parsed = parsed.replace('six', 's6x')
	parsed = parsed.replace('seven', 's7n')
	parsed = parsed.replace('eight', 'e8t')
	parsed = parsed.replace('nine', 'n9e')

	first = 0
	last = 0
	for char in parsed:
		if char.isnumeric():
			first = int(char)

	for char in parsed[::-1]:
		if char.isnumeric():
			last = int(char)

	total += last * 10 + first


print(total)
