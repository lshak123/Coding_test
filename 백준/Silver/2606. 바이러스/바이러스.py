import sys
input = sys.stdin.readline
N = int(input())
M = int(input())

node = [[] for _ in range(N+1)]
visited = [0]*(N+1)

for _ in range(M):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)

lst = []
def dfs(V):
    visited[V] = 1
    lst.append(V)
    for i in node[V]:
        if visited[i] == 0:
            dfs(i)

dfs(1)
print(len(lst)-1)