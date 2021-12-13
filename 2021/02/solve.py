input_file = "2021/02/input"

with open(input_file, "r") as f:
    data = f.read().splitlines()
data = [tuple(x.split()) for x in data]

x, y = 0, 0

for movement in data:
    move, amount = movement[0], int(movement[1])
    if move == "down": y += amount
    if move == "up": y -= amount
    if move == "forward": x += amount

print(x * y)

x, y, aim = 0, 0, 0

for movement in data:
    move, amount = movement[0], int(movement[1])
    if move == "down": aim += amount
    if move == "up": aim -= amount
    if move == "forward": 
        x += amount
        y += aim * amount

print(x * y)