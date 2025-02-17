a, b = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
answer = sorted(list(set(A)-set(B)))
if len(answer) == 0:
    print(0)
else:
    print(len(answer))
    for i in answer:
        print(i, end = ' ')