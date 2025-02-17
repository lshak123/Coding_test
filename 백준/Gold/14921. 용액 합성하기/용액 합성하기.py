n = int(input())
a = list(map(int,input().split()))
l, r = 0,n-1
answer = a[l]+a[r]
while l<r:
    tmp = a[l]+a[r]
    if abs(tmp)<abs(answer):
        answer = tmp
    if tmp<0:
        l+=1
    else:
        r-=1
print(answer)