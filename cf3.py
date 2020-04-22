def solve():
    n=int(input())
    arr=[int(v) for v in input().split()]
    i=0
    j=0
    ans=0
    while i<n:
        add=arr[i]
        while j<n and (arr[j]<0)==(arr[i]<0):
            add=max(add,arr[j])
            j+=1
        ans+=add
        i=j
    print(ans)


t=int(input())
for _ in range(t):
    solve()

	
	
	
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    # s = []
    temp = a[0]
    ans = 0
    for i in range(1, n):
        if a[i] > 0:
            if temp > 0:
                temp = max(temp, a[i])
            else:
                # s.append(temp)
                ans += temp
                temp = a[i]
        else:
            if temp < 0:
                temp = max(temp, a[i])
            else:
                # s.append(temp)
                ans += temp
                temp = a[i]
    # s.append(temp)
    # print(s)
    ans += temp
    print(ans)