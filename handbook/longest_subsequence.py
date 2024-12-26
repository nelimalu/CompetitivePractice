sequence = [6, 2, 5, 1, 7, 4, 8, 3]
lengths = [0] * len(sequence)


for k in range(len(sequence)):
	lengths[k] = max([i for x, i in enumerate(lengths) if sequence[x] < sequence[k]] + [0]) + 1


print(sequence[lengths.index(max(lengths))])
