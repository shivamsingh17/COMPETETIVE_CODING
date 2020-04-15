You are given N days to build a tower. Each day you are provided with a distinct brick size. For tower construction, you need to folllow below rules.
1. The bricks with larger sizes should be kept above.
2. The bricks with smaller sizes should be kept below.

So we mainly need to have the largest brick at the bottom and smallest at the top.

Input Format: The input line contains T, denoting the number of testcases. Each testcase contains two lines. The first line contains N, number of days. Second line contains size of bricks provided on ith day.

Output Format: You have to print the sizes of bricks which you can place at ith day in descending order separated by space.

Constraints:
1 <= T <= 100
1 <= N <= 106
1 <= size of brick <= 105

Sample Input:
2
5
4 5 1 2 3
6
7 8 2 9 5 3

Sample Output:
Not possible
5 4 
Not possible
Not possible
3 2 1
Not possible
Not possible
Not possible
9 8 7 
5 
3 2

Explanation:
Testcase 1:
On 1st day, you have brick of size 4 but you cannot place that as size of brick 5 is still remaining.
On 2nd day, you have bricks of size 4, 5 and thus you can place them keeping 5 at the bottom and 4 the top.
On 3rd and 4th day, you cannot place 1 and 2 brick size as size of brick 3 is not yet encountered.
On 5th day, you can place all the bricks of sizes 3 2 1 at the top of tower.

 
 
 
 for t in range(int(input())):
    N=int(input())
    l = list(map(int,input().split()))
    sor = sorted(l,reverse=True)
    i,j=0,0
    d={}
    while i<N:
        d[l[i]]=1
        f=0
    
        while (sor[j] in d.keys() and d[sor[j]]==1):
            print(sor[j],end=" ")
            f=1
            j+=1
            if j==N:
                break
        if f==1:
            print()
        else:
            print("Not possible")
        i+=1
        
    