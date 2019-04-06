import math

def twoPrimes(n):
    foundOne = False
    my_list = []
    i = 3
    for i in range(3,math.ceil(math.sqrt(n)),2):
        if n % i == 0:
            my_list.append(i)
            return (i,int(n/i))
    return (-1,-1)
T = int(input())
for t in range(1, T + 1):
        P, n = [int(s) for s in input().split()]
        numbers = [float(s) for s in input().split()]

        lastPair = twoPrimes(numbers[0])
        pairPrimes = [lastPair]

        newPrime = -1

        for i in range(1,n):
                x = numbers[i]/(lastPair[0])
                y = numbers[i]/(lastPair[1])
                if x.is_integer():
                        newPrime = x
                        lastPair = (int(lastPair[0]),int(x))
                else:
                        newPrime = y
                        lastPair = (int(lastPair[1]),int(y))
                pairPrimes.append(lastPair)

        listofIndexes = []
        temp = [x for t in pairPrimes for x in t]
        listofIndexes = list(set(temp))
        listofIndexes.sort()

        strList = []
        strList.append(chr(listofIndexes.index(pairPrimes[0][0])+65))
        strList.append(chr(listofIndexes.index(pairPrimes[0][1])+65))
        for i in range(1,len(pairPrimes)):
                strList.append(chr(listofIndexes.index(pairPrimes[i][1])+65))
        print("Case #{}: {}".format(t,''.join(strList)))