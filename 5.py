We all are familiar with social media platform Facebook, in present scenario almost everyone does have their profile on this platform. At the same time the existing person wants to connect with each other. Now for this problem we will have two types of query described as follows:
Query type addincircle: You will be given two persons and they will be added to each other circle.
Query type canwebecome: You will be given two persons and you have to find whether they can be added to their each other's circle or not. The two persons can be added to each other circle when they are directly/indirectly connected to each other.

Note: Initially persons are not connected in facebook hub. Person name will be of single alphabetic character in lowercase.

Input Format: The input line contains T, denoting the number of testcases. After each testcase the first line will contain N denoting the number of persons invloved in facebook hub initially and total number of queries Q separated by space. The very next line will contain N persons. At last there will be Q queries in separate line. The queries will be either of addincircle or arewefriends and two person names person1 and person2.  

Output Format: For each query of type arewefriends you need to return 1(true: if they are directly/indirectly connected) or 0(false: if they are not connected). 

Constraints: 
1 <= T <= 10
1 <= N <= 26
1<= Q <= 5*105
Total number of persons are equal to N

Sample Input:
2
4 4
a b c d
addincircle a b
addincircle c d
arewefriends a d
addincircle b d
4 5
p q r s
addincircle p q
addincircle p s
arewefriends q s
addincircle q r
arewefriends p r

Sample Output:
0
1
1



#code
def bfs(s,d):
    global g
    global N
    global arr
    color={}
    for i in range(N):
        color[arr[i]]='white'
    color[s] = "grey"
    queue = [s]
    f = False
    while len(queue)!=0:
        vertex = queue[0]
        if vertex==d:
            f = True
            break
        queue = queue[1:]
        color[vertex] = "black"
        neighbour = g[vertex]
        for n in neighbour:
            if color[n] == "white":
                queue.append(n)
                color[n] = "grey"
    return f
        
for _ in range(int(input())):
    N, Q=map(int,input().split())
    arr = list(input().split())
    
    g = {}
    for i in range(N):
        g[arr[i]]=[]
        
    for i in range(Q):
        q,s,d = input().split()
        if q=='addincircle':
            g[s].append(d)
            g[d].append(s)
        if q=='arewefriends':
            if bfs(s,d):
                print(1)
            else:
                print(0)
            