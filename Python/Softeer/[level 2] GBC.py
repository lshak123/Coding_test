import sys
input = sys.stdin.readline
lst1 = []
n, m = map(int, input().split())
for i in range(n):
    a, b = map(int, input().split())
    for _ in range(a):
        lst1.append(b)
max_num = 0
k = 0
for _ in range(m):
    a, b = map(int, input().split())
    for j in range(k, a+k):
        num = b - lst1[j]
        if num>=max_num:
            max_num = num
        k += 1
print(max_num)