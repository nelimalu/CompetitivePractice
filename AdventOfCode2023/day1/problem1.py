with open('../input.txt', 'r') as file:
	data = file.read().splitlines()


total = 0
for line in data:
	first = 0
	last = 0
	for char in line:
		if char.isnumeric():
			first = int(char)

	for char in line[::-1]:
		if char.isnumeric():
			last = int(char)

	total += last * 10 + first


print(total)
