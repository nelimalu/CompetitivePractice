num_students = int(input())

line1 = input().split()
line2 = input().split()


def solve():
	map1 = {}
	map2 = {}

	for i in range(num_students):
		if line1[i] == line2[i]:
			print('bad')
			return False

		if line1[i] in map1:
			if map1[line1[i]] != line2[i]:
				print('bad')
				return False
		elif line1[i] in map2:
			if map2[line1[i]] != line2[i]:
				print('bad')
				return False
		elif line2[i] in map1:
			if map1[line2[i]] != line1[i]:
				print('bad')
				return False
		elif line2[i] in map2:
			if map2[line2[i]] != line1[i]:
				print('bad')
				return False
		else:
			map1[line1[i]] = line2[i]
			map2[line2[i]] = line1[i]

	return True


if solve():
	print('good')
