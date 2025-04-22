from collections import deque

def read_input(filename):
    with open(filename, 'r') as f:
        return [list(map(int, line.split())) for line in f if line.strip()]

def write_output(filename, result):
    with open(filename, 'w') as f:
        f.write(str(result))

def build_graph(matrix):
    if not matrix or not matrix[0]:
        return None
    
    m, n = len(matrix), len(matrix[0])
    unsafe = [[False for _ in range(n)] for _ in range(m)]
    
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                unsafe[i][j] = True
                for dir_i, dir_j in [(-1,-1), (-1,0), (-1,1),
                               (0,-1),          (0,1),
                               (1,-1),  (1,0), (1,1)]:
                    neigbour_h, neighbour_v = i + dir_i, j + dir_j
                    if 0 <= neigbour_h < m and 0 <= neighbour_v < n:
                        unsafe[neigbour_h][neighbour_v] = True
    
    graph = {}
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    
    for i in range(m):
        for j in range(n):
            if not unsafe[i][j]:
                graph[(i, j)] = []
                for dir_x, dir_y in directions:
                    neigbour_h, neighbour_v = i + dir_x, j + dir_y
                    if 0 <= neigbour_h < m and 0 <= neighbour_v < n and not unsafe[neigbour_h][neighbour_v]:
                        graph[(i, j)].append((neigbour_h, neighbour_v))
    
    return graph, unsafe

def find_shortest_safe_path(matrix):
    graph, unsafe = build_graph(matrix)
    if not graph:
        return -1
    
    m, n = len(matrix), len(matrix[0])
    queue = deque()
    visited = {}

    for i in range(m):
        if (i, 0) in graph:
            queue.append((i, 0))
            visited[(i, 0)] = 1
    
    while queue:
        x, y = queue.popleft()
        
        if y == n - 1:
            return visited[(x, y)]
        
        for neighbor in graph.get((x, y), []):
            if neighbor not in visited:
                visited[neighbor] = visited[(x, y)] + 1
                queue.append(neighbor)
    
    return -1

if __name__ == "__main__":
    input_file = 'input.txt'
    output_file = 'output.txt'
    
    matrix = read_input(input_file)
    result = find_shortest_safe_path(matrix)
    write_output(output_file, result)