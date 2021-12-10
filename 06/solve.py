input_file = "06/input"

with open(input_file, "r") as f:
    data = f.read().splitlines()

data = [int(x) for x in data[0].split(',')]

days = 80
for i in range(days):
    zeroes = data.count(0)
    data = [x if x != 0 else 7 for x in data]
    data = [x - 1 for x in data]
    data += [8] * zeroes
print(len(data))

### Part Two
with open(input_file, "r") as f:
    data = f.read().splitlines()

data = [int(x) for x in data[0].split(',')]

alternative = [data.count(i) for i in range(9)]
print(alternative)

days = 256
for i in range(days):
    zeroes = alternative[0]
    alternative = alternative[1:] + [alternative[0]]
    alternative[6] += zeroes
print(alternative, sum(alternative))