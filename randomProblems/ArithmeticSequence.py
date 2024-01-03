class Sequence:
	def __init__(self, points, difference):
		self.points = points
		self.difference = difference
		self.solve_difference()

	def solve_difference(self):
		if len(self.points) >= 2:
			



class Grid:
	ROW_1 = [0, 1, 2]
	ROW_2 = [3, 4, 5]
	ROW_3 = [6, 7, 8]

	COL_1 = [0, 3, 6]
	COL_2 = [1, 4, 7]
	COL_3 = [2, 5, 8]

	def __init__(self, values):
		self.points = [None for _ in range(10)]
		self.parse(values)
		print(self.points)

	def parse(self, values):
		counter = 0
		for row in values:
			for item in row:
				try:
					self.points[counter] = int(item)
				except ValueError:
					self.points[counter] = None
				counter += 1


raw_values = [[n for n in input().split()] for _ in range(3)]
grid = Grid(raw_values)
