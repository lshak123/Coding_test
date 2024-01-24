import sys
input = sys.stdin.readline

n, m = map(int,input().split())

node = [[] for _ in range(n+1)]
visited = [0]*(n+1)

for _ in range(m):
    u, v = map(int,input().split())
    node[u].append(v)
    node[v].append(u)

def dfs(v):
    visited[v] = 1
    for i in node[v]:
        if visited[i] == 0:
            dfs(i)    

def bfs(v):
    visited[v] = 1
    q = [v]
    while q:
        cur = q.pop(0)
        for i in node[cur]:
            if visited[i] == 0:
                visited[i] = 1
                q.append(i)

answer = 0
for i in range(1,n+1):
    if visited[i] ==0:
        bfs(i)
        answer += 1
print(answer)