with open('../input.txt', 'r') as file:
	 data = file.read().split("\n\n")


class Rule:
	def __init__(self, range_start, domain_start, range_length):
		self.domain_start = domain_start
		self.domain_end = domain_start + range_length - 1
		self.range_start = range_start
		self.range_end = range_start + range_length - 1

	def __str__(self):
		return f"{self.domain_start} - {self.domain_end} -> {self.range_start} - {self.range_end}"




raw_seeds = [int(x) for x in data[0].split(": ")[1].split()]
raw_conversions = []

for i in range(1, 8):
	raw_conversions.append([[Rule(n[0], n[1], n[2]) for n in [int(y) for y in x.split()]] for x in data[i].split(":\n")[1].split("\n")])


print(raw_conversions)
