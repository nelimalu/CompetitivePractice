num_rocks = int(input())
rocks = [int(n) for n in input().split()]
unique_rocks = set(rocks)

max_rock = -1
max_rock_value = -1
for rock in unique_rocks:
	value = rock * rocks.count(rock)
	if value > max_rock_value:
		max_rock_value = value
		max_rock = rock

print(max_rock)
