import heapq
import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))
arr.sort()

heap = []
for i in arr:
    heapq.heappush(heap, i[1])
    if i[0] < len(heap):
        heapq.heappop(heap)
print(sum(heap))