import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
sensor = list(map(int,input().split()))
if k<n:
    sensor.sort()
    diff = []
    for i in range(len(sensor)-1):
        diff.append(sensor[i+1]-sensor[i])
    diff.sort()
    for _ in range(k-1):
        diff.pop()
    print(sum(diff))
else:
    print(0)