with open("../input.txt", 'r') as file:
	data = file.read().splitlines()


total = 0
for line in data:
	identity, info = line.split(":")
	identity = int(identity[5:])
	info = info.strip().split(";")
	info = [[point.split() for point in parcel.strip().split(", ")] for parcel in info]

	max_red = 0
	max_green = 0
	max_blue = 0
	for point in info:
		for parcel in point:
			if parcel[1] == "red" and int(parcel[0]) > max_red:
				max_red = int(parcel[0])
			if parcel[1] == "green" and int(parcel[0]) > max_green:
				max_green = int(parcel[0])
			if parcel[1] == "blue" and int(parcel[0]) > max_blue:
				max_blue = int(parcel[0])

	power = max_red * max_green * max_blue

	total += power


print(total)
