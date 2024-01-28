import sys
input = sys.stdin.readline
n, c  = map(int,input().split())
m = int(input())
boxes = []
for _ in range(m):
    boxes.append(list(map(int,input().split())))

truck = [c]*(n+1)
boxes.sort(key = lambda x:x[1])

answer = 0
for box in boxes:
    temp = c
    for i in range(box[0],box[1]):
        if temp>min(truck[i],box[2]):
            temp = min(truck[i],box[2])
    for i in range(box[0],box[1]):
        truck[i] -= temp
    answer += temp

print(answer)