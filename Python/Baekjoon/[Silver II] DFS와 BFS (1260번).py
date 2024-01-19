N, M, V = map(int, input().split())

node = [[] for _ in range(N+1)]
visited = [0]*(N+1)
dfs_lst = []

for _ in range(M):
    a,b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)

for i in node:
    i.sort()

def dfs(v):
    visited[v] = 1
    dfs_lst.append(v)
    for i in node[v]:
        if visited[i] == 0:
            dfs(i)
    
dfs(V)

for i in range(len(visited)):
    visited[i] = 0

bfs_lst = []
def bfs(v):
    visited[v] = 1
    bfs_lst.append(v)
    q = [v]

    while q:
        cur = q.pop(0)
        for i in node[cur]:
            if visited[i] == 0:
                visited[i] = 1
                bfs_lst.append(i)
                q.append(i)
bfs(V)

for i in dfs_lst:
    print(i, end = ' ')
print()
for i in bfs_lst:
    print(i, end = ' ')