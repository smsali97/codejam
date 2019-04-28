import sys

T, W = [int(s) for s in input().strip().split()]

i = 0
days = [0 for i in range(6)]
print(i)
sys.stdout.flush()
days[0] = int(input().strip()) 
i += 1
cum_days = days[0] 
while(i != W):
    print(i)
    sys.stdout.flush()
    D = int(input().strip())
    if ( D == -1):
        exit()
    days[i] = D - cum_days
    cum_days += D
    i += 1
print(" ".join(map(str,days)))