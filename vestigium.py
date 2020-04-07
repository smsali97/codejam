# Code Jam 2020 lets gooo

T = int(input())

for t in range(1, T + 1):
    N = int(input())

    matrix = []
    for i in range(N):
        matrix.append([])
        matrix[i] = list(map(int,input().split()))

    row_ctr = 0
    col_ctr = 0
    trace = 0
    for i in range(N):
        if not len(set(matrix[i])) == N:
            row_ctr += 1
    for i in range(N):
        if not len(set([row[i] for row in matrix])) == N:
            col_ctr += 1
    trace = sum([matrix[i][j] for j in range(N) for i in range(N) if i == j])
    print("Case #{}: {} {} {}".format(t,trace,row_ctr,col_ctr))