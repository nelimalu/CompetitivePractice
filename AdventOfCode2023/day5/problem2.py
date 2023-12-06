with open('../input.txt', 'r') as file:
	 data = file.read().split("\n\n")

raw_seeds = [int(x) for x in data[0].split(": ")[1].split()]
raw_conversions = []

for i in range(1, 8):
	raw_conversions.append([[int(y) for y in x.split()] for x in data[i].split(":\n")[1].split("\n")])


cache = []


minimum = float("inf")
print(len(raw_seeds) // 2)
for i in range(len(raw_seeds) // 2):
	print(i / (len(raw_seeds) // 2))
	for x, seed in enumerate(range(raw_seeds[i * 2], raw_seeds[i * 2] + raw_seeds[i * 2 + 1])):
		print(x / raw_seeds[i * 2 + 1])
		if seed not in cache:

			out = seed
			# print("\nseed:", seed)
			for conversion in raw_conversions:
				# seed to soil

				for _map in conversion:
					range_start = _map[0]
					domain_start = _map[1]
					range_length = _map[2]
					# print("  ", out, range_start, domain_start, range_length)

					if out >= domain_start and out < domain_start + range_length:
						out = range_start + (out - domain_start)
						break

			if seed not in cache:
				cache.append(seed)
			if out < minimum:
				minimum = out


print("Final answer:", minimum)
