import sys
input = sys.stdin.readline

N, K = map(int, input().split())
cs = 0
ls = list(range(1, N+1))
answer = []

while len(ls) != 0:
    cs += K
    while cs > len(ls):
        cs = cs % len(ls)
    if cs == 0:
        cs = len(ls)
    answer.append(ls.pop(cs-1))
    cs -= 1

print('<',end='')
for e in answer[:-1]:
    print(e, end=', ')
print(answer[-1], end='')
print('>')