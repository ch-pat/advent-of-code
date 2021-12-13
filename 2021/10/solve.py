input_file = "2021/10/input"

with open(input_file, "r") as f:
    data = f.read().splitlines()

opening_chars = "{[(<"
closing_chars = "}])>"

scores = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

opener_to_closer = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}

openers = []
expected_closers = []
corrupted_chars = []
corrupted_lines = []
for line in data:
    for char in line:
        if char in opening_chars:
            openers.append(char)
            expected_closers.append(opener_to_closer[char])
        elif char in closing_chars:
            last_opened = openers.pop()
            expected = expected_closers.pop()
            if char != expected:
                corrupted_chars += [char]
                corrupted_lines += [line]
                break
    openers = []
    expected_closers = []


print(corrupted_chars)
print(sum([scores[char] for char in corrupted_chars]))

### Part Two
completion_scores = {")": 1, "]": 2, "}": 3, ">": 4}
incomplete_lines = [line for line in data if line not in corrupted_lines]
line_scores = []
for line in incomplete_lines:
    for char in line:
        if char in opening_chars:
            openers.append(char)
            expected_closers.append(opener_to_closer[char])
        elif char in closing_chars:
            last_opened = openers.pop()
            expected = expected_closers.pop()
    score = 0
    while expected_closers:
        current = expected_closers.pop()
        score = score * 5 + completion_scores[current]
    line_scores += [score]
    openers = []

print(sorted(line_scores)[len(line_scores) // 2])