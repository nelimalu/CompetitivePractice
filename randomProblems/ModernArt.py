cols = int(input())
rows = int(input())
num_strokes = int(input())

gold_locs = [[] for _ in range(rows)]

default_row = [x for x in range(rows)]
default_column = [x for x in range(cols)]

for i in range(num_strokes):
	stroke = input().split()
	if stroke[0] == "C":
		col = int(stroke[1]) - 1
		gold_locs[col] = [num for num in default_column if num not in gold_locs[col]]

	if stroke[0] == "R":
		row = int(stroke[1]) - 1
		for x, col in enumerate(gold_locs):
			if row in col:
				col.remove(row)
			else:
				col.append(row)

total = 0
for i in gold_locs:
	total += len(i)

print(total)
