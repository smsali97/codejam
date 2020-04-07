T = int(input())

for t in range(1, T + 1):
    timings = []
    for i in range(int(input())):
        start_t, end_t = map(int,input().split())
        timings.append((start_t,end_t,i))
    sorted_timings = sorted(timings)

    ending_J = 0
    ending_C = 0
    ordering = []
    possibile = None
    for timing in sorted_timings:
        start_t, end_t, index = timing
        if ending_J <= start_t:
            ending_J = end_t
            ordering.append(('J',index))
            continue
        if ending_C <= start_t:
            ending_C = end_t
            ordering.append(('C',index))
            continue
        else:
            possibile = 'IMPOSSIBLE'
            break
    
    ordering.sort(key=lambda x: x[1])
    ordering = [ x[0] for x in ordering]
    if possibile is None:
        possibile = ''.join(ordering)
        
    print("Case #{}: {}".format(t,possibile))
        
        
        
