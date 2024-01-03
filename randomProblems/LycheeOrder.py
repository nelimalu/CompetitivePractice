class Lychee:
	def __init__(self, name, ripeness):
		self.name = name
		self.ripeness = int(ripeness)

	def __int__(self):
		return self.ripeness

	def __str__(self):
		return self.name


num_lychee, num_queries = map(int, input().split())

lychees = [Lychee(*input().split()) for i in range(num_lychee)]
lychees.sort(key=int, reverse=True)
queries = [int(input()) for n in range(num_queries)]

for query in queries:
	print(str(lychees[query - 1]))

