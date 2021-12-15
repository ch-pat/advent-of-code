input_file = "2021/15/input"

with open(input_file, "r") as f:
    data = f.read().splitlines()

import math

# data = """1163751742
# 1381373672
# 2136511328
# 3694931569
# 7463417111
# 1319128137
# 1359912421
# 3125421639
# 1293138521
# 2311944581""".splitlines()

ORTHOGONAL = [(i, j) for i in (-1, 0, 1) for j in (-1, 0, 1) if (i, j) != (0, 0) and (abs(i), abs(j)) != (1, 1)]
def get_adjacents(graph, x, y):
    min_x, min_y = 0, 0
    max_x, max_y = len(graph[0]), len(graph)

    adjacents = [(x + i, y + j) for (i, j) in ORTHOGONAL if min_x <= x + i < max_x and min_y <= y + j < max_y]
    return adjacents

def get_next(distances, shortest_path_found, candidates):
    min_distance_found = math.inf
    for v in candidates:
        if distances[v] < min_distance_found:
            min_distance_found = distances[v]
            next_vertex = v
    return next_vertex


graph = [[int(x) for x in line] for line in data]

shortest_path_found = set([])
all_vertices = {(i, j) for i in range(len(graph[0])) for j in range(len(graph))}
distances = {x: math.inf for x in all_vertices}
distances[(0, 0)] = 0
candidates = {(0, 0)}


while shortest_path_found != all_vertices:
    v = get_next(distances, shortest_path_found, candidates)
    shortest_path_found.add(v)
    candidates.remove(v)
    for adj in get_adjacents(graph, v[0], v[1]):
        # Candidates are only on the frontier border
        if adj not in shortest_path_found:
            candidates.add(adj)
        weight = graph[adj[1]][adj[0]]
        if adj not in shortest_path_found and distances[adj] > distances[v] + weight:
            distances[adj] = distances[v] + weight

print(distances[(len(graph) - 1, len(graph[0]) - 1)])

### Part two
small_graph = [[int(x) for x in line] for line in data]
size = len(small_graph)  # Graph is square

graph = [[0 for x in range(size * 5)] for line in range(size * 5)]
for x, _ in enumerate(small_graph[0]):
    for y, _ in enumerate(small_graph):
        for i in range(5):
            for j in range(5):
                value = small_graph[y][x] + i + j
                if value >= 10:
                    value -= 9
                graph[y + size*j][x + size*i] = value

shortest_path_found = set([])
all_vertices = {(i, j) for i in range(len(graph[0])) for j in range(len(graph))}
distances = {x: math.inf for x in all_vertices}
distances[(0, 0)] = 0
candidates = {(0, 0)}

while shortest_path_found != all_vertices:
    v = get_next(distances, shortest_path_found, candidates)
    shortest_path_found.add(v)
    candidates.remove(v)
    for adj in get_adjacents(graph, v[0], v[1]):
        if adj not in shortest_path_found:
            # Candidates are only on the frontier border
            # Keeping the set of candidates small drastically reduces 'get_next()' time
            candidates.add(adj)
        weight = graph[adj[1]][adj[0]]
        if adj not in shortest_path_found and distances[adj] > distances[v] + weight:
            distances[adj] = distances[v] + weight

print(distances[(len(graph) - 1, len(graph[0]) - 1)])