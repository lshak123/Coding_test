import sys
input = sys.stdin.readline
num = list(map(int,input().split()))
if num == [i for i in range(1,9)]:
    print('ascending')
elif num == [i for i in range(8,0,-1)]:
    print('descending')
else:
    print('mixed')