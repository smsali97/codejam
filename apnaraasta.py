T = int(input())
east = 'E'
south = 'S'

for t in range(1, T + 1):
    N = int(input())

    path =[[('X','X') for i in range(N)] for j in range(N)]
    directions = input()
    
    i, j = 0, 0
    prev_i, prev_j = 0, 0
    for direction in directions:
        i, j = prev_i, prev_j
        if direction is south:
            i += 1
        else:
            j += 1
        # mark path as visited
        path[i][j] = (prev_i,prev_j)
        prev_i, prev_j = i, j

    # for a in range(N):
    #     for b in range(N):
    #         print(path[a][b],end=' ')
    #     print()

    # SESSEEEEEESSSS

    source = (0,0,'')
    my_path = []
    frontier = [source]
    visited = set()

    prev = {}

    while not len(frontier) is 0:
        curr = frontier.pop()
        visited.add(curr)
        r, c, d = curr
        if r == N - 1 and c == N -1:
            break
        print(r,c,end=' ')
        neighbors = []
        if not r + 1 == N and not path[r+1][c] == (r,c):
            neighbors.append((r+1,c,south))
        if not c + 1 == N and not path[r][c+1] == (r,c):
            neighbors.append((r,c+1,east))

        for neighbor in neighbors:
            if not neighbor in visited:
                frontier.append(neighbor)
                prev[curr] = neighbor
    
    while curr is not source:
        t = prev[curr]
        my_path.insert(0,t[2])
        curr = t
    print("Case #{}: {}".format(t,''.join(my_path)))