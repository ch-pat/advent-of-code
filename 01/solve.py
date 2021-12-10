input_file = "01/input"

with open(input_file, "r") as f:
    data = f.read().splitlines()
data = [int(x) for x in data]

increases = 0
for i in range(len(data) - 1):
    if data[i] < data[i + 1]:
        increases += 1
print(increases)

window3_increases = 0
window = 3
for i in range(len(data) - 3):
    window1 = sum(data[i:i + 3])
    window2 = sum(data[i + 1:i + 4])
    if window1 < window2:
        window3_increases += 1
print(window3_increases)