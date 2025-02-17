n = int(input())
rope = []
for _ in range(n):
    rope.append(int(input()))
rope = sorted(rope,reverse=True)
answer = 0
for i,j in enumerate(rope):
    tmp = j*(i+1)
    answer = max(tmp, answer)
print(answer)