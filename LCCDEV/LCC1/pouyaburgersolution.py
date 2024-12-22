opposite = {
	"C": "J",
	"J": "C",
	"R": "S",
	"S": "R" 
}
openers = ["C", "R"]
closers = ["J", "S"]


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


def burgerify(brackets):
	brackets = brackets.replace('(', 'C')
	brackets = brackets.replace(')', 'J')
	brackets = brackets.replace('[', 'R')
	brackets = brackets.replace(']', 'S')
	return brackets


inp = input()
print(burgerify(inp))
print(solve(burgerify(inp)))

