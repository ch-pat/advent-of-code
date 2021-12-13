input_file = "2021/13/input"

with open(input_file, "r") as f:
    data = f.read().splitlines()

blank_line_index = data.index("")
coords = data[:blank_line_index]
instructions = data[blank_line_index + 1:]
coords = [(int(x.split(',')[0]), int(x.split(',')[1]))  for x in coords]
instructions = [x[11:].split('=') for x in instructions]
instructions = [(x[0], int(x[1])) for x in instructions]

max_x = max([x[0] for x in coords]) + 1
max_y = max([x[1] for x in coords]) + 1

def get_clean_matrix(max_x, max_y):
    return [[0 for _ in range(max_x)] for _ in range(max_y)]

def place_points(matrix, points):
    for p in points:
        matrix[p[1]][p[0]] = 1

def print_matrix(matrix):
    result = ""
    counter = 0
    for j in range(len(matrix)):
        for i in range(len(matrix[0])):
            if matrix[j][i] == 1:
                result += "@"
                counter += 1
            else:
                result += " "
        result += "\n"
    print(result)
    return counter

def fold(matrix, axis, value):
    max_x = len(matrix[0])
    max_y = len(matrix)

    if axis == "x":
        new_matrix = get_clean_matrix(value, max_y)
        for i in range(value + 1):
            for j in range(max_y):
                if matrix[j][i] == 1:
                    new_matrix[j][i] = 1
        for i in range(value, max_x):
            for j in range(max_y):
                if matrix[j][i] == 1:
                    new_matrix[j][max_x - 1 - i] = 1
                    
    if axis == "y":
        new_matrix = get_clean_matrix(max_x, value)
        for i in range(max_x):
            for j in range(value + 1):
                if matrix[j][i] == 1:
                    new_matrix[j][i] = 1
        for i in range(max_x):
            for j in range(value, max_y):
                if matrix[j][i] == 1:
                    new_matrix[max_y - 1 - j][i] = 1

    return new_matrix


matrix = get_clean_matrix(max_x, max_y)
place_points(matrix, coords)
first_fold_axis, first_fold_value = instructions[0]
new_matrix = fold(matrix, first_fold_axis, first_fold_value)
print(len(new_matrix[0]), len(new_matrix))
print(print_matrix(new_matrix))

### Part Two
matrix = get_clean_matrix(max_x, max_y)
place_points(matrix, coords)
for instruction in instructions:
    axis, value = instruction
    matrix = fold(matrix, axis, value)

print_matrix(matrix)