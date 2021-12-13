input_file = "2021/05/input"

with open(input_file, "r") as f:
    data = f.read().splitlines()

class Segment():
    def __init__(self, segment_representation):
        a, b = segment_representation.split(' -> ')
        self.x1, self.y1 = a.split(',')
        self.x2, self.y2 = b.split(',')
        self.x1 = int(self.x1)
        self.x2 = int(self.x2)
        self.y1 = int(self.y1)
        self.y2 = int(self.y2)
        self.representation = segment_representation

    def is_orthogonal(self):
        return self.is_horizontal() or self.is_vertical()

    def is_horizontal(self):
        return self.y1 == self.y2

    def is_vertical(self):
        return self.x1 == self.x2

    def get_points(self):
        if self.is_horizontal():
            a = min(self.x1, self.x2)
            b = max(self.x1, self.x2)
            return set([(i, self.y1) for i in range(a, b + 1)])
        elif self.is_vertical():
            a = min(self.y1, self.y2)
            b = max(self.y1, self.y2)
            return set([(self.x1, i) for i in range(a, b + 1)])
        else:
            """With the given input, non orthogonal lines are always at a 45 degree angle"""
            #TODO not working for negative diagonals
            length = abs(self.x1 - self.x2)
            leftmost_point = (self.x1, self.y1) if self.x1 < self.x2 else (self.x2, self.y2)
            rightmost_point = (self.x1, self.y1) if self.x1 >= self.x2 else (self.x2, self.y2)
            positive = leftmost_point[1] < rightmost_point[1]
            start_x, start_y = leftmost_point
            if positive:
                return set([(start_x + i, start_y + i) for i in range(length + 1)])
            else:
                return set([(start_x + i, start_y - i) for i in range(length + 1)])



segments = [Segment(r) for r in data]

orthogonal_segments = [s for s in segments if s.is_orthogonal()]
points = dict()
for segment in orthogonal_segments:
    segment_points = segment.get_points()
    for point in segment_points:
        if not point in points:
            points[point] = 1
        else:
            points[point] += 1

count = 0
for p in points:
    if points[p] > 1:
        count += 1
print(count)

points = dict()
### Part Two

for segment in segments:
    segment_points = segment.get_points()
    for point in segment_points:
        if not point in points:
            points[point] = 1
        else:
            points[point] += 1

count = 0
for p in points:
    if points[p] > 1:
        count += 1
print(count)