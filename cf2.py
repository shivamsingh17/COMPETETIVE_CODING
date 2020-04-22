for t in range(int(input())):
    n = int(input())
    
    half = n//2
    if  half%2:
        print('NO')
    else:
        a = [0]*n
        evensum = 0
        t=2
        for i in range(half):
            a[i]=t
            evensum+=t
            t+=2
        t = 1
        for i in range(half,n-1):
            a[i]=t
            evensum-=t
            t+=2
        a[-1]=evensum
        print('YES')
        print(" ".join(map(str,a)))