from random import choice
from random import randint
import pyperclip
import json

'''
( -> Confetticus
) -> Janitorum
[ -> Rainborimus
] -> Sunshinio
'''

opposite = {
	"C": "J",
	"J": "C",
	"R": "S",
	"S": "R" 
}
openers = ["C", "R"]
closers = ["J", "S"]
all_possible = openers + closers


def solve(spellset: str) -> str:
	stack = [spellset[0]]

	for spell in spellset[1:]:
		if spell in closers and len(stack) == 0:
			return "embarrassing"
		if spell in closers and opposite[spell ] == stack[-1]:
			stack.pop()
		elif spell in openers:
			stack.append(spell)
		else:
			return "embarrassing"
	return "impressive" if len(stack) == 0 else "embarrassing"


def generate() -> str:
	approx_length = 1_400_000  # 1_400_000 => 1mil
	stack = []
	output = ""
	for i in range(approx_length):
		if randint(1,3) == 1:
			if randint(1,2) == 1:
				output += "C"
				stack.append("J")
			else:
				output += "R"
				stack.append("S")
		elif len(stack) != 0:
			if randint(1,approx_length // 2) == 1:
				stack.pop()
				output += choice(all_possible)
			else:
				output += stack.pop()

	output += "".join(stack[::-1])
	return output


def migrate():
	data = []
	with open('testcases.json', 'r') as file:
		data = json.loads(file.read())
	
	for x, testcase in enumerate(data):
		with open(f'testcases/{x}.in', 'w') as file:
			file.write(testcase['in'])
		with open(f'testcases/{x}.out', 'w') as file:
			file.write(testcase['out'])


def main():
	counter = 38
	while True:
		problem = generate()
		solution = solve(problem)

		print("-- GENERATED --")
		# print("out:", problem)
		# pyperclip.copy(problem)
		print("length:", len(problem))
		print("solution:", solution)

		a = input("Save this problem? - ")
		if a.startswith('y'):
			counter += 1
			with open(f'testcases/{counter}.in', 'w') as file:
				file.write(problem)
			with open(f'testcases/{counter}.out', 'w') as file:
				file.write(solution)
		if a.startswith('q'):
			break


main()
# migrate()

