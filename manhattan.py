import numpy as np
import math
T = int(input())

north = 'N'
south = 'S'
east = 'E'
west = 'W'

for t in range(1, T + 1):
    P, Q = [int(s) for s in input().strip().split()]
    grid = np.zeros(shape=(Q,Q))

    max_val = -1
    max_x = -1
    max_y = -1

    for i in range(P):
        a = [s for s in input().strip().split()]
        x = int(a[0])
        y = int(a[1])
        direction = a[2]

        if direction is east:
            for i in range(Q):
                for j in range(x+1,Q):
                    grid[i][j] += 1
        elif direction is west:
            for i in range(Q):
                for j in range(x-1,0,-1):
                    grid[i][j] += 1
        elif direction is north:
            for i in range(y+1,Q):
                for j in range(Q):
                    grid[i][j] += 1
        elif direction is south:
            for i in range(y-1,0,-1):
                for j in range(Q):
                    grid[i][j] += 1
                    
        for i in range(Q):
            for j in range(Q):
                if grid[i][j] >= max_val and abs(x):
                    max_val = grid[i][j]
                    max_x = i
                    max_y = j
    # print(grid)
    print("Case #{}: {} {}".format(t,max_y,max_x))