convert = "ABCDEFGHIJ"


class Cell:
	def __init__(self, data):
		self.raw_data = data
		self.value = None
		self.pointers = []
		self.parse()

	def parse(self):
		try:
			self.value = int(self.raw_data)
		except ValueError:
			for i in self.raw_data.split("+"):
				self.pointers.append((int(i[1]) - 1, convert.index(i[0])))

	def getValue(self, depth):
		if self.value is not None:
			return self.value
		
		total = 0
		for pointer in self.pointers:
			if pointer in depth:
				self.value = '*'
				return '*'

			value = grid[pointer[1]][pointer[0]].getValue(depth + [pointer])
			if value == '*':
				self.value = '*'
				return '*'
			total += value

		self.value = total
		return total


grid = [[Cell(x) for x in input().split()] for _ in range(10)]

for y, row in enumerate(grid):
	for x, cell in enumerate(row):
		print(cell.getValue([(x, y)]), end=" ")
	print()

