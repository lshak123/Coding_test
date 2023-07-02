import sys
def f(x,n):
    if n == 1:
        return x
    elif n%2 == 0:
        res = f(x, n/2)
        return (res*res)%1000000007
    else:
        res = f(x, n//2)
        return (res*res*x)%1000000007

k, p, n = map(int,input().split())
answer = f(p, n*10)*k
print(answer%1000000007)