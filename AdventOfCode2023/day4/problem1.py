with open("../input.txt", 'r') as file:
	data = file.read().splitlines()


total = 0
for line in data:
	winning, yours = [x.strip().split() for x in line.split(": ")[1].split(" | ")]
	
	count = 0
	for point in yours:
		if point in winning:
			count += 1

	if count > 0:
		total += 2 ** (count - 1)


print(total)
