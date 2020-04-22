import math
for t in range(int(input())):
    n = int(input())
    k = 2
    while True:
        x = n/(pow(2,k)-1)
        if math.floor(x) == math.ceil(x):
            break
        k+=1
    print(int(x))