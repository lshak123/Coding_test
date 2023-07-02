import sys
input = sys.stdin.readline
label ={"0" : '1110111',
        '1' : '0010001',
        '2' : '0111110',
       '3' : '0111011',
       '4' : '1011001',
       '5' : '1101011',
       '6' : '1101111',
       '7' : '1110001',
       '8' : '1111111',
       '9' : '1111011',
       '_' : '0000000'}
t = int(input())
for _ in range(t):
    a, b = input().split()
    k = max(len(a),len(b))
    zero_a, zero_b = k-len(a), k-len(b)
    a = "_"*zero_a+a
    b = "_"*zero_b+b
    answer = 0
    for i in range(k):
        for j in range(7):
            if label[a[i]][j] != label[b[i]][j]:
                answer += 1
    print(answer)