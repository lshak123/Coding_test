def solution(tickets):
    tickets.sort(key=lambda x:x[1])
    dic = {}
    for key,value in tickets:
        if key not in dic:
            dic[key] = []
            dic[key].append(value)
        else:
            dic[key].append(value)

    stack = ['ICN']
    answer = []

    while stack:
        cur = stack[-1]
        if cur in dic and len(dic[cur]) != 0:
            stack.append(dic[cur].pop(0))
        else:
            answer.append(stack.pop())
    return answer[::-1]