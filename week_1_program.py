# code wars solution
def path_finder(maze):
    matrix = list(map(list, maze.splitlines()))
    length = len(matrix)
    s = (0,0)
    t = (length - 1,length - 1)
    level = {s: 0}
    parent = {s: 0}
    i = 1
    frontier = [s]
    while frontier:
        next = []
        for u in frontier:
            x,y = u
            for v in Adj[u]:
                if v not in level:
                    level[v] = i
                    parent[v] = u
                    next.append(v)
        frontier = next
        i+=1
    return path_finder(maze)
#previous attempt
import random
import pprint
def make_make(size, lvl, st):
    # make a matrix with random ints
    matrix = [[random.randint(0,10) for row in range(size)] for col in range(size)]
    # loop through the matrix
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            # if element is > lvl = a free space
            if matrix[row][col] > lvl:
                matrix[row][col] = '.' # . = free space
                # else element is a wall
            else:
                matrix[row][col] = '|'
    x,y = st
    matrix[x][y] = "S"
    return matrix
# call our function to make a maze
maze = make_make(10, 2, [0,0])
pprint.pprint(maze)
# find all edges for node N
def find_edges(matrix, node):
    x,y = node
    edges = []
    length = len(matrix)
    # add conditions for nw, sw, ne, se
    for x,y in (x, y+1), (x, y-1), (x+1, y), (x-1, y):
        if 0 <= x < length and 0 <= y < length:
            # check if matrix[x][y] is a free space
            if matrix[x][y] == '.':
                edges.append([x,y])
    return edges

def bfs (start, maze):
    queue = [start]
    explored = []
    while queue:
        # FIFO
        next = queue.pop(0)
        if next not in explored:
            explored.append(next)
            edges = find_edges(maze, next)
            for edge in edges:
                if edge not in explored:
                    queue.append(edge)
            path = None
    return explored
print(bfs((0,0), maze))
