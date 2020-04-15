"""

	Given the vacant seats of N rows of a theatre represented by an array row[], maximize the profit that can be made by selling the tickets to K people waiting in a queue. The cost of a seat in the ith row is the number of current vacant seats in the ith row.
Note: It could be possible that number of people are greater than the available vacant seats, and hence it may not be possible to seat all people.

Input:
The first line of input contains T denoting the number of testcases. T testcases follow. Each testcase contains two lines of input. The first line contains size of array N and number of people K, and the second line contains the elements of the array.

Output:
For each testcase, in a new line, print the maximum profit.

Constraints:
1 <= T <= 100
1 <= N <= 104
0 <= K <= 104
0 <= arri <= 105

Examples:
Input:
2
3 3
2 1 1
5 6
2 3 4 5 1
Output:
4
22


"""
for _ in range(int(input())):
	n,k=map(int,input().split())
    l=list(map(int,input().split()))
    l=[-x for x in l]
    heapify(l)
    ans=0
    while k>0 and l:
        t=-heappop(l)
        if t==0:
            break
        if l:
            x=-heappop(l)
        else:
            x=0
        y=t-x+1
        if x==0:
            y-=1
        if y>k:
            y=k
        k-=(y)
        ans+=((t*y)-(y*(y-1)//2))
        heappush(l,-x)
        heappush(l,-x+1)
    print(ans)
        
        
            