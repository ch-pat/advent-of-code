input_file = "2021/14/input"

with open(input_file, "r") as f:
    data = f.read().splitlines()

polymer = data[0]
insertion_rules = [x.split(' -> ') for x in data[2:]]
insertion_rules = {k: k[0] + v + k[1] for (k, v) in insertion_rules}

#################### Naive full string solution #################################
new_polymer = polymer
for _ in range(10):
    pairs = []
    for i in range(len(new_polymer) - 1):
        pairs += [new_polymer[i:i + 2]]
    last_letter = pairs[-1][-1]
    new_polymer = "".join([insertion_rules[x][:-1] for x in pairs]) + last_letter
print(new_polymer, len(new_polymer))

from collections import Counter

counts = Counter(new_polymer)
print(counts)
print(max(counts.values()) - min(counts.values()))
#################################################################################

print("###Part Two")
pairs = {polymer[i:i + 2]: 0 for i in range(len(polymer) - 1)}
for i in range(len(polymer) - 1):
    pairs[polymer[i:i + 2]] += 1

insertion_rules = {k: [v[0:2], v[1:3]] for (k, v) in insertion_rules.items()}

def add_pair(pairs, pair, amount):
    if pair in pairs:
        pairs[pair] += amount
    else:
        pairs[pair] = amount


for _ in range(40):
    # Save current amounts to detract (otherwise we zero out too much) and pairs to iterate 'simultaneously'
    current_pairs = [p for p in pairs if pairs[p]]
    amounts = [pairs[p] for p in pairs if pairs[p]]
    for p, amount in zip(current_pairs, amounts):
        # All starting pairs (amount) get converted to two pairs according to the rule
        pairs[p] -= amount
        for rule in insertion_rules[p]:
            add_pair(pairs, rule, amount)

print(pairs)
letters = set([])
last_letter = polymer[-1]

# Prepare letter counts dict
for pair in pairs:
    letters.add(pair[0])
    letters.add(pair[1])
letter_counts = {k: 0 for k in letters}

# Fill counts dict; 
# NOTE! We only take the first letter of each pair, because the second letter would get repeated in the next pair.
# For this reason we also add a copy of the very last letter at the end.
for pair in pairs:
    letter = pair[0]
    letter_counts[letter] += pairs[pair]
letter_counts[last_letter] += 1

print(letter_counts)
print(max(letter_counts.values()) - min(letter_counts.values()))
