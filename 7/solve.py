input_file = "7/input"

with open(input_file, "r") as f:
    data = f.read().splitlines()
data = [int(x) for x in data[0].split(',')]

from math import inf

def fuel_cost(crabs, position):
    total_fuel = 0
    for crab in crabs:
        total_fuel += abs(crab - position)
    return total_fuel

minimum = min(data)
maximum = max(data)

least_fuel = inf
for i in range(minimum, maximum + 1):
    fuel = fuel_cost(data, i)
    if fuel < least_fuel:
        least_fuel = fuel

print(least_fuel)

### Part Two

def fuel_cost_triangle(crabs, position):
    total_fuel = 0
    for crab in crabs:
        steps = abs(crab - position)
        total_fuel += steps * (steps + 1) // 2
    return total_fuel

least_fuel = inf
for i in range(minimum, maximum + 1):
    fuel = fuel_cost_triangle(data, i)
    if fuel < least_fuel:
        least_fuel = fuel

print(least_fuel)
