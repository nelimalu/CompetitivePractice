height, width = map(int, input().split())

screen = [list(input()) for _ in range(height)]

counter = 0
for y in range(height):
	for x, item in enumerate(screen[y]):
		if item == "#":
			mirrored_x = width - x - 1
			mirrored_y = height - y - 1

			if screen[y][mirrored_x] == '.':
				screen[y][mirrored_x] = '#'
				counter += 1

			if screen[mirrored_y][x] == '.':
				screen[mirrored_y][x] = '#'
				counter += 1

			if screen[mirrored_y][mirrored_x] == '.':
				screen[mirrored_y][mirrored_x] = '#'
				counter += 1


print(counter)
for line in screen:
	print("".join(line))


