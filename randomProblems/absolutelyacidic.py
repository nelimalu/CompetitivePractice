import sys

num_sensors = int(sys.stdin.readline())
readings = [0 for _ in range(1000)]

for _ in range(num_sensors):
	readings[int(sys.stdin.readline()) - 1] += 1


largest_frequency = -1
largest_readings = []
second_largest_frequency = -1
second_largest_readings = []

# print(readings)

# index is the reading
# value is the amount of times that reading occured
for reading, frequency in enumerate(readings):
	#print(frequency, largest_frequency)
	if frequency > largest_frequency:
		second_largest_readings = largest_readings[:]
		second_largest_frequency = [largest_frequency][:][0]
		largest_readings = [reading + 1]
		largest_frequency = frequency
	elif frequency == largest_frequency:
		largest_readings.append(reading + 1)

	if frequency < largest_frequency and frequency > second_largest_frequency:
		second_largest_readings = [reading + 1]
		second_largest_frequency = frequency
	elif frequency < largest_frequency and frequency == second_largest_frequency:
		second_largest_readings.append(reading + 1)


#print("--")
#print(largest_readings)
#print(second_largest_readings)
#print("--")

if len(largest_readings) > 1:
	print(max(largest_readings) - min(largest_readings))
else:
	if second_largest_frequency == 0:
		print(0)
	else:
		print(max(
			abs(max(largest_readings) - min(second_largest_readings)), abs(max(second_largest_readings) - min(largest_readings))
		))
