import sys
input = sys.stdin.readline

n = int(input())
chu = list(map(int, input().split()))
chu.sort()

target = 1

for num in chu:
    if target < num:
        break

    target += num

print(target)