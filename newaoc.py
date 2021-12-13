#! /usr/bin/python3.9
import os, argparse

parser = argparse.ArgumentParser(description='Prepare directory for the next advent of code problem')
parser.add_argument('Year', metavar='N', type=int, nargs='?',
                    help='Year for which you are creating a new problem directory')

year = str(parser.parse_args().Year)

if not year:
    print("No year specified. Please specify a year.")
    exit()

if year not in os.listdir():
    os.mkdir(year)
    problem = "01"
else:
    latest = max((int(x) for x in os.listdir(year)))
    problem = str(latest + 1)
    if len(problem) == 1:
        problem = "0" + problem

os.mkdir(f"{year}/{problem}")

solve = f"""input_file = "{year}/{problem}/input"

with open(input_file, "r") as f:
    data = f.read().splitlines()
"""

with open(f"{year}/{problem}/solve.py", "w+") as f:
    f.write(solve)

with open(f"{year}/{problem}/input", "w+") as f:
    f.write("")

print("Created new problem dir.")