width, height = map(int, input().split())
current_x = 0
current_y = 0

while True:
    raw = input()
    if raw == "0 0":
        break

    x, y = map(int, raw.split())

    current_x += x
    current_y += y

    if current_x < 0:
        current_x = 0
    elif current_x > width:
        current_x = width
    if current_y < 0:
        current_y = 0
    elif current_y > height:
        current_y = height

    print(current_x, current_y)

