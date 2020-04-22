from collections import deque
import sys
input = sys.stdin.readline
inf = int(1e9)
for i in range(int(input())):
    n, m, a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    c -= 1
    cost = list(map(int, input().split()))
    g = [[] for _ in range(n)]
    for i in range(m):
        a2, b2 = map(int, input().split())
        g[a2 - 1].append(b2 - 1)
        g[b2 - 1].append(a2 - 1)
    def bfs(st):
        Q = deque(maxlen=n)
        lv = [-1] * n
        Q.append(st)
        lv[st] = 0
        while Q:
            cur = Q.popleft()
            for to in g[cur]:
                if lv[to] == -1:
                    lv[to] = lv[cur] + 1
                    Q.append(to)
        return lv
    lvA = bfs(a)
    lvB = bfs(b)
    lvC = bfs(c)
    # print(lvA, lvB, lvC)
    ans = int(1e18)
    cost.sort()
    cost.insert(0, 0)
    for i in range(1, len(cost)):
        cost[i] += cost[i - 1]
    # print(cost)
    for i in range(n):
        d1 = lvB[i]
        d2 = lvA[i] + lvC[i]
        if d1 + d2 >= len(cost):
            continue
        # print(f'i={i}, d1={d1}, d2={d2}')
        ans = min(ans, cost[d1] * 2 + cost[d1 + d2] - cost[d1])
    print(ans)

    

	
	
	
import sys
from collections import deque
from itertools import accumulate


def bfs(n, s, links):
    q = deque([(0, s)])
    visited = set()
    distances = [0] * n
    while q:
        d, v = q.popleft()
        if v in visited:
            continue
        visited.add(v)
        distances[v] = d
        q.extend((d + 1, u) for u in links[v] if u not in visited)
    return distances


ipt = list(map(int, sys.stdin.buffer.read().split()))
buf = []
t = ipt[0]
k = 1
INF = 10 ** 18
for _ in range(t):
    n, m, a, b, c = ipt[k:k + 5]
    ppp = ipt[k + 5:k + 5 + m]
    uv = ipt[k + 5 + m:k + 5 + 3 * m]
    k += 5 + 3 * m
    ppp.sort()
    ppp_acc = [0] + list(accumulate(ppp))
    links = [set() for _ in range(n)]
    for u, v in zip(uv[0::2], uv[1::2]):
        u -= 1
        v -= 1
        links[u].add(v)
        links[v].add(u)
    # print(links)
    from_a = bfs(n, a - 1, links)
    from_b = bfs(n, b - 1, links)
    from_c = bfs(n, c - 1, links)
    # print(from_a)
    # print(from_b)
    # print(from_c)

    ans = INF
    for fa, fb, fc in zip(from_a, from_b, from_c):
        fs = fa + fb + fc
        # print(fa, fb, fc, fs, ppp_acc[fb] + ppp_acc[fs] if fs <= m else '-')
        if fs > m:
            continue
        ans = min(ans, ppp_acc[fb] + ppp_acc[fs])

    buf.append(ans)

print('\n'.join(map(str, buf)))
