num_measurements = int(input())
measurements = sorted([int(x) for x in input().split()])

is_even = int(len(measurements) % 2 == 1)
lowest = measurements[:((len(measurements) // 2) + is_even)][::-1]
highest = measurements[((len(measurements) // 2) + is_even):]

for a, b in zip(lowest, highest):
	print(a, b, end=" ")

if is_even:
	print(lowest[-1])
