with open("../input.txt", 'r') as file:
	data = file.read().splitlines()


total = 0
for line in data:
	identity, info = line.split(":")
	identity = int(identity[5:])
	info = info.strip().split(";")
	info = [[point.split() for point in parcel.strip().split(", ")] for parcel in info]

	valid = True
	for point in info:
		for parcel in point:
			if (parcel[1] == "red" and int(parcel[0]) > 12) or \
				(parcel[1] == "green" and int(parcel[0]) > 13) or \
				(parcel[1] == "blue" and int(parcel[0]) > 14):
				valid = False
				break

	if valid:
		total += identity


print(total)
