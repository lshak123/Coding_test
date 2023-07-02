import sys
input = sys.stdin.readline
m, n, k = map(int, input().split())
secret = "".join(list(map(str,input().split())))
inp = "".join(list(map(str,input().split())))
if inp.find(secret) == -1:
    print('normal')
else:
    print('secret')