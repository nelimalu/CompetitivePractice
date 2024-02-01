ichika_mins, ichika_max_food, num_restaurants = map(int, input().split())

restaurants = [[int(x) for x in input().split()] + [c] for _, c in enumerate(range(num_restaurants))]

# restaurant object
# impression, time, food, id

def solve(current_restaurant, visited, time_used, units_eaten):
	time_used += current_restaurant[1]
	units_eaten += current_restaurant[2]

	max_impression = 0
	for restaurant in restaurants:
		if current_restaurant[3] not in visited:
			new_impression = solve(restaurant, visited + [current_restaurant[3]], time_used, units_eaten)
			if new_impression > max_impression:
				max_impression = new_impression

	return max_impression + current_restaurant[0]


def start():
	max_impression = 0
	for restaurant in restaurants:
		new_impression = solve(restaurant, [restaurant[3]], 0, 0)
		if new_impression > max_impression:
			max_impression = new_impression

	return max_impression


print(start())
