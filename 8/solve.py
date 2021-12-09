input_file = "8/input"

with open(input_file, "r") as f:
    data = f.read().splitlines()

inputs, outputs = [], []

for line in data:
    i, o = line.split(' | ')
    i = i.split()
    o = o.split()
    inputs += [i]
    outputs += [o]


unique_lengths = (2, 4, 3, 7)
count = 0
for o in outputs:
    for element in o:
        if len(element) in unique_lengths:
            count += 1
print(count)

### Part Two

def get_obvious_numbers(numbers):
    numbers_dict = {}
    numbers_dict[0] = None
    numbers_dict[6] = None
    numbers_dict[9] = None
    numbers_dict[2] = None
    numbers_dict[5] = None
    numbers_dict[3] = None
    for n in numbers:
        if len(n) == 2:
            numbers_dict[1] = set(n)
        elif len(n) == 4:
            numbers_dict[4] = set(n)
        elif len(n) == 3:
            numbers_dict[7] = set(n)
        elif len(n) == 7:
            numbers_dict[8] = set(n)
    return numbers_dict

def get_ambiguous_numbers(numbers_dict, numbers):
    eight = numbers_dict[8]
    four = numbers_dict[4]
    one = numbers_dict[1]
    two = None
    tleft_bright = None
    top_bottom_bleft: set = eight - four
    center_tleft: set = four - one
    done = []
    while not all((numbers_dict[i] for i in range(10))):
        for n in numbers:
            sectors = set(n)
            if len(n) == 5:
                #can be 2, 5, 3
                # Recognize two
                if top_bottom_bleft.issubset(sectors):
                    numbers_dict[2] = sectors
                    two = sectors
                    tleft_bright = eight - two
                if tleft_bright:
                    if tleft_bright.issubset(sectors):
                        numbers_dict[5] = sectors
                if numbers_dict[5] and numbers_dict[2] and numbers_dict[5] != sectors and numbers_dict[2] != sectors:
                    numbers_dict[3] = sectors
            elif len(n) == 6:
                #can be 0, 6, 9
                if not top_bottom_bleft.issubset(sectors):
                    numbers_dict[9] = sectors
                if numbers_dict[9] and numbers_dict[9] != sectors and center_tleft.issubset(sectors):
                    numbers_dict[6] = sectors
                if numbers_dict[6] and numbers_dict[9] and numbers_dict[6] != sectors and numbers_dict[9] != sectors:
                    numbers_dict[0] = sectors
    return numbers_dict

displayed_numbers = []
for i, o in zip(inputs, outputs):
    numbers_dict = get_obvious_numbers(i)
    numbers_dict = get_ambiguous_numbers(numbers_dict, i)
    inverse_dict = {frozenset(v):k for k, v in numbers_dict.items()}
    current_number = 0
    for power, n in enumerate(o):
        current_number += int(inverse_dict[frozenset(n)]) * 10 ** (3 - power)
    displayed_numbers += [current_number]
print(displayed_numbers)
print(sum(displayed_numbers))