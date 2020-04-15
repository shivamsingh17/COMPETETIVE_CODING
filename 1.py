"""You are a package delivery driver for some company X. There are N cities (numbered from 1 to N) that you need to visit to distribute the packages. The roads that connect the cities may be of different lengths and thus it would cost different amounts of gasoline to travel to different cities. Now, you are a money conscious driver and thus you try to visit each city while taking paths that minimize your overall gasoline costs. Also, if you are driving back to a city already visited by you, then your drive back to that city is paid by the company so you don't need include it in your expenditure.
You need to find the minimum total cost of gasoline such that you visit all the cities.
Note: It is guaranteed that every city is connected to every other city either directly or indirectly.

Input:
The first line of input contains T denoting the number of test cases. T test cases follow. Each test case contains N+1 lines of input. The first line contains number of the cities N. The next N lines contain gas price required to cover distance between each city to every other city. If there is no direct path between two cities then the cost is denoted by -1.

Output:
For each test case, in new line, print the total minimum cost of gasoline.

Constraints:
1 <= T <= 100
1 <= N <= 200
-1 <= gasPrice <= 105

Examples:
Input:
2
3
0 5 -1
5 0 1
-1 1 0
2
0 8
8 0
Output:
6
8
"""

#Solution:
from collections import defaultdict

def getRoot(i,par):
    while i!=par[i]:
        i = par[i]
    return i

def find(a,b,par):
    return getRoot(a,par)==getRoot(b,par)

def doUnion(a,b,par,size):
    if find(a,b,par):
        return -1
    r1 = getRoot(a,par)
    r2 = getRoot(b,par)
    s1 = size[r1]
    s2 = size[r2]
    if s1 > s2:
        par[r2] = r1
        size[r1] += s2
    else:
        par[r1] = r2
        size[r2] += s1
    return 1

t = int(stdin.readline())
while t>0:
    n = int(stdin.readline())
    a = []
    for i in range(n):
        a.append( list(map(int,stdin.readline().split())) )
    d = []
    for i in range(n):
        for j in range(i):
            if i!=j and a[i][j]>0:
                d.append( [a[i][j],i+1,j+1] )
    d = sorted(d)
    
    par = [ i+1 for i in range(n) ]
    par = [0] + par
    size = [ 1 for i in range(n)]
    size = [0] + size

    s = 0;
    for i in range(len(d)):
        x = doUnion(d[i][1],d[i][2],par,size);
        if x==1:
            s += d[i][0];
        
    stdout.write("{}\n".format(s))
    t-=1
