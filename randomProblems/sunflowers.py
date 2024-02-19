num_flowers = int(input())
rows = [[int(x) for x in input().split()] for _ in range(num_flowers)]


def rotate(array):
	return list(zip(*array[::-1]))


if rows[0][1] > rows[0][0] and rows[1][0] > rows[0][0]:  # not rotated
	for row in rows:
		print(*row)

elif rows[0][1] < rows[0][0] and rows[1][0] > rows[0][0]:
	for row in rotate(rotate(rotate(rows))):
		print(*row)

elif rows[0][1] > rows[0][0] and rows[1][0] < rows[0][0]:
	for row in rotate(rows):
		print(*row)

else:
	for row in rotate(rotate(rows)):
		print(*row[::-1])
