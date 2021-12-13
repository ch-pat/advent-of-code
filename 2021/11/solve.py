input_file = "2021/11/input"

with open(input_file, "r") as f:
    data = f.read().splitlines()

data = [[int(x) for x in line] for line in data]
octopi = data
flash_map = [[0 for x in line] for line in data]

SURROUNDING = [(i, j) for i in (-1, 0, 1) for j in (-1, 0, 1) if (i, j) != (0, 0)]
 
def get_surrounding(octopi, x, y):
    min_x, min_y = 0, 0
    max_x, max_y = len(octopi[0]), len(octopi)

    adjacents = [(x + i, y + j) for (i, j) in SURROUNDING if min_x <= x + i < max_x and min_y <= y + j < max_y]
    return adjacents


def increase_adjacent(octopi, x, y):
    adjacents = get_surrounding(octopi, x, y)
    for i, j in adjacents:
        if octopi[j][i] != 0:
            octopi[j][i] += 1


def increase_all(octopi):
    for i in range(len(octopi[0])):
        for j in range(len(octopi)):
            octopi[j][i] += 1

def check_and_reset(octopi, counter, flashing_octopi):
    for i in range(len(octopi[0])):
        for j in range(len(octopi)):
            if octopi[j][i] >= 10:
                flashing_octopi += [(i, j)]
                counter[0] += 1
                octopi[j][i] = 0

def step(octopi, counter):
    print()
    increase_all(octopi)
    flashing_octopi = []
    check_and_reset(octopi, counter, flashing_octopi)
    while flashing_octopi:
        x, y = flashing_octopi.pop()
        increase_adjacent(octopi, x, y)
        check_and_reset(octopi, counter, flashing_octopi)
    for line in octopi:
        print(line)


counter = [0]
simultaneous_flash = []
for i in range(1000):
    step(octopi, counter)
    if i == 99:
        final_count = counter[0]
    ### Check for part two; increase range
    if all((x == 0 for line in octopi for x in line)):
        simultaneous_flash = i + 1
        break
print(final_count)
print(simultaneous_flash)