import pdb
from helpers import normalize, blur

def initialize_beliefs(grid):
    height = len(grid)
    width = len(grid[0])
    area = height * width
    belief_per_cell = 1.0 / area
    beliefs = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(belief_per_cell)
        beliefs.append(row)
    return beliefs

def sense(color, grid, beliefs, p_hit, p_miss):
    new_beliefs = []
    height = len(beliefs)
    width = len(beliefs[0])
    for j in range(height):
        row = []
        for i in range(width):
            belief = beliefs[j][i]
            if color == grid[j][i]:
                row.append(belief * p_hit)
            else:
                row.append(belief * p_miss)
        new_beliefs.append(row)
    new_beliefs_normalized = normalize(new_beliefs)
    return new_beliefs

def move(dy, dx, beliefs, blurring):
    height = len(beliefs) - 1
    width = len(beliefs[0]) - 1
    new_G = [[0.0 for i in range(width)] for j in range(height)]
    for i, row in enumerate(beliefs):
        for j, cell in enumerate(row):
            new_i = (i + dy ) % width
            new_j = (j + dx ) % height
            #pdb.set_trace()
            new_G[int(new_i)][int(new_j)] = cell
    return blur(new_G, blurring)