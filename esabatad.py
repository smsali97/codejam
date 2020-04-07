import sys
MAX_QUERIES = 150 
T, B = map(int,input().split())


for _ in range(T):
    arr = [{0:0,1:0} for _ in range(B)]
    for i in range(MAX_QUERIES):
        position = i % B
        print(position)
        sys.stdout.flush()
        answer = int(input())
        arr[position][answer] = arr[position][answer] + 1 
    
    bits = []
    for item in arr:
        if item[0] > item[1]:
            bits.append(0)
        else:
            bits.append(1)
    print(''.join(bits))
    sys.stdout.flush()
    response = input()
    if response == 'Y': continue
    else: exit(1)





    