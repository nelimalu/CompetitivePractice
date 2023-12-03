from math import ceil, floor

max_cows, num_farms, num_visits = map(int, input().split())
cows = [int(input()) for _ in range(num_farms)]
visits = sorted([int(input()) for _ in range(num_visits)])
print(visits)
cache = {}


def solve_farms(num_cows, depth, end):
    if depth == end:
        return 1

    if num_cows in cache:
        return cache[num_cows]

    if num_cows <= max_cows:
        if num_cows * 2 <= max_cows:
            return solve_farms(num_cows * 2, depth + 1, end)
        else:
            a = solve_farms(num_cows, depth + 1, end)
            b = solve_farms(num_cows, depth + 1, end)
            cache[num_cows * 2] = a + b
            return a + b

    a = solve_farms(ceil(num_cows / 2), depth + 1, end)
    b = solve_farms(floor(num_cows / 2), depth + 1, end)
    cache[num_cows] = a + b
    if depth in visits:
        print(a + b)
    return a + b


for cow in cows:
    solve_farms(cow, 0, max(visits))

