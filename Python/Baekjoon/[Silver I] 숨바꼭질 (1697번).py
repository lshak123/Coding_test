n, k = map(int,input().split())

visited = [0]*100001

def bfs(v):
    q = [v]
    while q:
        cur = q.pop(0)
        if cur == k:
            return visited[cur]
        for i in [cur-1, cur+1,cur*2]:
            if 0<=i<=100000 and not visited[i]:
                visited[i] = visited[cur]+1
                q.append(i)
                
print(bfs(n))