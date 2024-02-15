# prefix sum!
import sys

max_weight = int(sys.stdin.readline())
num_cars = int(sys.stdin.readline())

output = -1

done = False
cars = [0, 0, 0, int(sys.stdin.readline())]
if cars[3] > max_weight:
	done = True
	output = 0

for i in range(3, num_cars + 2):
	if done:
		sys.stdin.readline()
		continue

	cars.append(cars[i] + int(sys.stdin.readline()))
	if cars[i + 1] - cars[i - 3] > max_weight:
		done = True
		output = i - 2

if not done:
	output = num_cars

print(output)
