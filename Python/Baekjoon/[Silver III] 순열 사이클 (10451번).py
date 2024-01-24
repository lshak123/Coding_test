t = int(input())

def dfs(v):
    visited[v] = 1
    next_node = node[v]
    if visited[next_node] == 0:
        dfs(next_node)
        
for _ in range(t):
    n = int(input())
    node = [[] for _ in range(n+1)]
    visited = [0]*(n+1)
    answer = 0
    lst = list(map(int,input().split()))
    for i in range(1,n+1):
        node[i] = lst[i-1]

    for j in range(1,n+1):
        if visited[j] == 0:
            dfs(j)
            answer += 1

    print(answer)
