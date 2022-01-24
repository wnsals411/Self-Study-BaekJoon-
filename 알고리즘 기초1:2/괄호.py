import sys

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    s = list(input().rstrip())
    a = []

    if s.count('(') != s.count(')'):
        print('NO')
        continue
    else:
        for e in s:
            if e == '(':
                a.append(1)
            else:
                a.append(-1)
                if sum(a) < 0:
                    print('NO')
                    break

    if len(s) == len(a):
        print('YES')