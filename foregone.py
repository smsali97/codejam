T = int(input())


for t in range(1, T + 1):
    n = input()
    N = len(n)

    arr = []
    for i in range(len(n)-1,-1,-1):
        if n[i] is '4':
            arr.append(10 ** (N-1-i))
    s_sum = sum(arr)
    c_sum = int(n) - s_sum

    print("Case #{}: {} {}".format(t,s_sum,c_sum))