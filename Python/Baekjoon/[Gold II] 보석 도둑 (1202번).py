import heapq
import sys
input = sys.stdin.readline

N, K = map(int,input().split())
lst = []
for _ in range(N):
    heapq.heappush(lst,list(map(int,input().split())))
bags = []
for _ in range(K):
    bags.append(int(input()))

bags.sort()
answer =0
temp_lst = []
for bag in bags:
    while lst and bag >= lst[0][0]:
        heapq.heappush(temp_lst,-heapq.heappop(lst)[1])
    if temp_lst:
        answer -= heapq.heappop(temp_lst)
    elif not lst:
        break
print(answer)