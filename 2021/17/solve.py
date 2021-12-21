input_file = "2021/17/input"

with open(input_file, "r") as f:
    data = f.read().splitlines()

data = data[0].replace("target area: ", "").split(", ")
min_x, max_x = data[0][2:].split("..")
min_y, max_y = data[1][2:].split("..")
min_x = int(min_x)
min_y = int(min_y)
max_x = int(max_x)
max_y = int(max_y)

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"
    
class Rectangle():
    def __init__(self, topleft: Point, bottomright: Point):
        self.topleft = topleft
        self.bottomright = bottomright

    def is_inside(self, point: Point):
        if self.topleft.x <= point.x <= self.bottomright.x and self.bottomright.y <= point.y <= self.topleft.y:
            return True
        return False

class Probe():
    def __init__(self, start: Point, velocity: Point):
        self.start = start
        self.velocity = velocity

    def launch(self, target: Rectangle) -> list:
        trajectory = []
        current_point = self.start
        start_v = self.velocity.x, self.velocity.y
        while current_point.x <= target.bottomright.x and current_point.y >= target.bottomright.y:
            trajectory += [current_point]
            next_x = current_point.x + self.velocity.x
            next_y = current_point.y + self.velocity.y
            if self.velocity.x > 0:
                self.velocity.x -= 1
            elif self.velocity.x <0:
                self.velocity.x += 1
            self.velocity.y -= 1
            current_point = Point(next_x, next_y)
        # print(f"Exited, current point is {current_point}, while bounds: {target.bottomright} (start is {target.topleft})")
        # if any((target.is_inside(p) for p in trajectory)):
        #     print(start_v, trajectory)
        return trajectory

    def get_highest_point_on_hit(self, target: Rectangle):
        trajectory = self.launch(target)
        if trajectory:
            hit = any([target.is_inside(p) for p in trajectory])
            if hit:
                return max([p.y for p in trajectory])



topleft = Point(min_x, max_y)
bottomright = Point(max_x, min_y)
target = Rectangle(topleft, bottomright)
highest_results = []

for x in range(17, max_x + 1):
    for y in range(min_y, -max_y*2):
        probe = Probe(Point(0,0), velocity=Point(x, y))
        highest_results += [probe.get_highest_point_on_hit(target)]

print(max([r for r in highest_results if r is not None]))

### Part Two
print(len([r for r in highest_results if r is not None]))