types = {}

for i in input():
	if i not in types:
		types[i] = 1
	else:
		types[i] += 1

vals = types.values()
maximum = max(vals)
gap = maximum - (sum(vals) - maximum) - 1
print(gap if gap > 0 else 0)
