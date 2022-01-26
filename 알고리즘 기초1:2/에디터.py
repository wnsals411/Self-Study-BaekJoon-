import sys
input = sys.stdin.readline

s = list(input().rstrip())
cs = len(s)
right = []
M = int(input())

for _ in range(M):
    c = input().split()
    
    if c[0] == 'L':
        if cs > 0:
            cs -= 1
            right.append(s.pop())
    elif c[0] == 'D':
        if len(right) != 0:
            cs += 1
            s.append(right.pop())
    elif c[0] == 'B':
        if cs > 0:
            cs -= 1
            s.pop()
    else:
        s.append(c[1])
        cs += 1

a = ''

for e in s:
    a += e

for i in range(len(right)-1, -1, -1):
    a += right[i]

print(a)