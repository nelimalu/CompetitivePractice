with open("../input.txt", 'r') as file:
	data = file.read().splitlines()


cards = []
instances = [1] * len(data)


for line in data:
	winning, yours = [x.strip().split() for x in line.split(": ")[1].split(" | ")]
	
	count = 0
	for point in yours:
		if point in winning:
			count += 1

	cards.append(count)



for i in range(len(instances)):
	for j in range(i + 1, min(i + cards[i] + 1, len(data))):
		instances[j] += instances[i]

print(sum(instances))
