def solution(n, computers):

    def dfs(v):
        visited[v] = 1
        for i in node[v]:
            if visited[i] == 0:
                dfs(i)

    node = [[] for _ in range(len(computers))]
    visited = [0]*(len(computers))

    for n,i in enumerate(computers):
        for y,j in enumerate(i):
            if j == 1:
                node[n].append(y)
    answer = 0
    for i in range(len(node)):
        if visited[i] == 0:
            dfs(i)
            answer+=1
    return answer