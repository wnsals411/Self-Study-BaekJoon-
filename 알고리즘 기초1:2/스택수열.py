n = int(input())
stack = []
answer = []
cur = 1
flag = 0
for _ in range(n):
    num = int(input())
    while cur <= num:
        stack.append(cur)
        answer.append('+')
        cur += 1
    
    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    else:
        print('NO')
        flag = 1
        break

if flag == 0:
    for e in answer:
        print(e)