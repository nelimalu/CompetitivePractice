def tile(width):
	if width % 2 == 1:
		return 0
	return 3 ** (int(width) / 2) + 2 ** (int(width) / 4)


def main():
	for i in range(5):
		print(int(tile(int(input()))) % 1_000_000)


main()
