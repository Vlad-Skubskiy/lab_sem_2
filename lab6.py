from collections import defaultdict

def find_max_experience_path(input_file='input.txt', output_file='output.txt'):
    with open(input_file, "r") as file:
        lines = file.readlines()
        Level = int(lines[0])
        pyramid = [list(map(int, line.split())) for line in lines[1:]]

    graph = defaultdict(list)
    values = {}
    for lvl in range(Level):
        for idx in range(lvl + 1):
            values[(lvl, idx)] = pyramid[lvl][idx]

    for lvl in range(Level - 1):
        for idx in range(lvl + 1):
            graph[(lvl + 1, idx)].append((lvl, idx))
            graph[(lvl + 1, idx + 1)].append((lvl, idx))

    visited = set()
    topologic_order = []

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        topologic_order.append(node)

    for col in range(Level):
        node = (Level - 1, col)
        if node not in visited:
            dfs(node)

    topologic_order = topologic_order[::-1]

    dp = defaultdict(int)
    prev = {}
    for col in range(Level):
        dp[(Level - 1, col)] = values[(Level - 1, col)]

    for node in topologic_order:
        for neighbor in graph[node]:
            if dp[node] + values[neighbor] > dp[neighbor]:
                dp[neighbor] = dp[node] + values[neighbor]
                prev[neighbor] = node

    start = max(((0, col) for col in range(1)), key=lambda x: dp[x])
    result = dp[start]

    path = []
    current = start
    while current in prev:
        path.append(current)
        current = prev[current]
    path.append(current)
    path.reverse()

    with open(output_file, "w") as file:
        file.write(str(result) + "\n")
        file.write(' -> '.join(f"{values[pos]}" for pos in path) + "\n")

find_max_experience_path()