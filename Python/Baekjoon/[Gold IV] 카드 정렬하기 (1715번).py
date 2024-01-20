import heapq
import sys
input = sys.stdin.readline

N = int(input())
heap = []
answer = 0
for i in range(N):
    heap.append(int(input()))

heapq.heapify(heap)
while len(heap)>1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    heapq.heappush(heap,a+b)
    answer += a+b
print(answer)