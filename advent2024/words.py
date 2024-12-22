import requests

content = requests.get("https://raw.githubusercontent.com/LDNOOBW/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words/refs/heads/master/en").content.decode().splitlines()

available_letters = list("ABCDEFXYMOIHFKVRGUZTPLS ")
extra_words = ['BIG C', 'KP','BIG D','BIGGIE','ERICA','WONJAM','BRIAN','ANTO','SAILESH','ADAM', 'ZEFF']
possible_words = []

for word in content + extra_words:
	works = True
	for letter in list(word):
		if letter.upper() not in available_letters:
			works = False
			break
	if works:
		possible_words.append(word)


print(possible_words)
