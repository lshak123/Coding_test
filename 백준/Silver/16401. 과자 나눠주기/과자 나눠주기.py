M, N = map(int,input().split())
snacks = list(map(int,input().split()))
s, e = 1, max(snacks)
while s<=e:
    mid = (s+e)//2
    cnt = 0

    for i in snacks:
        cnt += i//mid
    
    if cnt >= M:
        s = mid+1
    else:
        e = mid-1
print(e)