input_file = "09/input"

with open(input_file, "r") as f:
    data = f.read().splitlines()

data = [[int(x) for x in line] for line in data]

def get_adjacent_points(data, x, y):
    min_x = 0
    min_y = 0
    max_x = len(data[0])
    max_y = len(data)
    up = (x, y - 1) if y - 1 >= min_y else None
    down = (x, y + 1) if y + 1 < max_y else None
    left = (x - 1, y) if x - 1 >= min_x else None
    right = (x + 1, y) if x + 1 < max_x else None
    adjacents = [up, down, left, right]
    return [x for x in adjacents if x]

def is_low_point(data, x, y):
    adjacents = get_adjacent_points(data, x, y)
    return all((data[y][x] < data[j][i] for (i, j) in adjacents))

low_points = []

for i, row in enumerate(data):
    for j, col in enumerate(row):
        if is_low_point(data, j, i):
            low_points += [(j, i)]

risk_levels = [data[j][i] + 1 for i, j in low_points]
print(risk_levels)
print(sum(risk_levels))

### Part Two

def get_adjacents_in_basin(data, x, y):
    adjacents = get_adjacent_points(data, x, y)
    value = data[y][x]
    result = []
    for point in adjacents:
        if 9 > data[point[1]][point[0]] >= value:
            result += [point]
    return result


def find_basin_points(data, low_point):
    basin = [low_point]
    stack = [low_point]
    while stack:
        current = stack.pop()
        for point in get_adjacents_in_basin(data, current[0], current[1]):
            if point not in basin:
                basin += [point]
                stack += [point]
    return basin

basins = []
for point in low_points:
    basins += [find_basin_points(data, point)]

lengths = [len(x) for x in basins]
s = sorted(lengths)
print(s[-1] * s[-2] * s[-3])