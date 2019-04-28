import math

T = int(input())
for t in range(1, T + 1):
        P, n = [int(s) for s in input().strip().split()]
        numbers = [int(s) for s in input().strip().split()]

        primeList = []
        for i in range(n-1):
                my_gcd = math.gcd(numbers[i],numbers[i+1])
                if i == 0:
                        primeList.append(int(numbers[i]/my_gcd))
                primeList.append(my_gcd)
                if i == n - 2:
                        primeList.append(int(numbers[i+1]/my_gcd))
        
        listofIndexes = sorted(list(set(primeList)))
        indexer = {}
        for p in listofIndexes:
                indexer[]
        strList = []
        
        for prime in primeList:
                strList.append(chr(listofIndexes.index(prime)+65))
        print("Case #{}: {}".format(t,''.join(strList)))