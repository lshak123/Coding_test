import sys
input = sys.stdin.readline

F, S, G, U, D = map(int,input().split())
visited = [0]*(F+1)

def dfs(v):
    q = [v]
    visited[v] = 1
    while q:
        cur = q.pop(0)
        if cur == G:
            return visited[cur]-1
        for i in [cur+U,cur-D]:
            if i<=F and i>0 and visited[i] == 0:
                q.append(i)
                visited[i]=visited[cur]+1
    if visited[G] == 0:
        return 'use the stairs'
    
print(dfs(S))