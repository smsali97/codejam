possible = 'POSSIBLE'
impossible = 'IMPOSSIBLE'


T = int(input())
for t in range(1, T + 1):
    R = int(input())
    C = int(input())

    visited = [[False for i in range(R)] for j in range(C)]
    

    print("Case #{}: {}".format(t,x)