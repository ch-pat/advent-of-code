input_file = "2021/12/input"

with open(input_file, "r") as f:
    data = f.read().splitlines()

# data = """start-A
# start-b
# A-c
# A-b
# b-d
# A-end
# b-end""".splitlines()

node_links = [x.split('-') for x in data]
nodes = set([])
for i, j in node_links:
    nodes.add(i)
    nodes.add(j)

class Graph():
    def __init__(self, nodes, pairs):
        self.nodes: set = nodes
        self.adjacent = {k: [] for k in nodes}
        for pair in pairs:
            a, b = pair
            self.adjacent[a] += [b]
            self.adjacent[b] += [a]
    
    def print_adjacency(self):
        for k in self.adjacent:
            print(f"{k}: {self.adjacent[k]}")

    def visit(self, start, end, visited, path, paths):
        if start == start.lower():
            visited += [start]
        path += [start]
        if start == end:
            paths += [path[:]]
        else:
            for node in self.adjacent[start]:
                if node not in visited:
                    self.visit(node, end, visited, path, paths)
        path.pop()
        if start == start.lower():
            visited.remove(start)

    def visit_2(self, start, end, visited, path, paths):
        if start == start.lower():
            visited += [start]
        path += [start]
        if start == end:
            paths += [path[:]]
        else:
            for node in self.adjacent[start]:
                if node == 'start' or node == 'end':
                    if node not in visited:
                        self.visit_2(node, end, visited, path, paths)
                elif not any((visited.count(x) == 2 for x in self.nodes)):
                    self.visit_2(node, end, visited, path, paths)
                elif node not in visited:
                    self.visit_2(node, end, visited, path, paths)

        path.pop()
        if start == start.lower():
            visited.remove(start)

graph = Graph(nodes, node_links)
path = []
paths = []
visited = []
graph.visit('start', 'end', visited, path, paths)

for p in paths:
    print(p)

print(len(paths))

### Part Two
path = []
paths = []
visited = []
graph.visit_2('start', 'end', visited, path, paths)

for p in paths:
    print(p)

print(len(paths))
