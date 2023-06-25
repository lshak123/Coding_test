import sys
input = sys.stdin.readline
n, m = map(int, input().split())
parent = [i for i in range(n+1)]

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

lst = []
for i in range(m):
    lst.append(list(map(int, input().split())))

lst.sort(key = lambda x:x[2])


cost = 0
c = 0
for i in lst:
    if find(i[0]) != find(i[1]):
        parent[find(i[0])] = find(i[1])
        cost += i[2]
        c = i[2]
        
print(cost-c)