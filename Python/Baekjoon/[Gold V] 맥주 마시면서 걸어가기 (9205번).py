import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    x, y = map(int,input().split())
    store = []
    for _ in range(n):
        store.append(list(map(int,input().split())))
    festival_x,festival_y = map(int,input().split())
    visited = [0]*(n+1)

    def bfs():
        q = [[x,y]]
        while q:
            cur_x,cur_y = q.pop(0)
            if abs(cur_x-festival_x)+abs(cur_y-festival_y) <=1000:
                return 'happy'
            for i in range(n):
                if visited[i] == 0:
                    store_x,store_y = store[i]
                    if abs(cur_x-store_x)+abs(cur_y-store_y)<=1000:
                        visited[i] = 1
                        q.append([store_x,store_y])
        return 'sad'

    print(bfs())