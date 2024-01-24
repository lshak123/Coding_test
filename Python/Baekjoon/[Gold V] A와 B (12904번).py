s = input()
t = input()

answer = 0
while len(s) <= len(t):
    if s != t:
        if t[-1] == 'A':
            t = t[:-1]
        else:
            t = t[:-1]
            t= t[::-1]
    else:
        answer = 1
        break

print(answer)