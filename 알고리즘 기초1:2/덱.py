import sys
input = sys.stdin.readline
dq = []
N = int(input())
for _ in range(N):
    c = input().split()
    if c[0] == 'push_front':
        dq.insert(0, c[1])
    elif c[0] == 'push_back':
        dq.append(c[1])
    elif c[0] == 'pop_front':
        if len(dq) != 0:
            print(dq.pop(0))
        else:
            print(-1)
    elif c[0] == 'pop_back':
        if len(dq) != 0:
            print(dq.pop())
        else:
            print(-1)
    elif c[0] == 'size':
        print(len(dq))
    elif c[0] == 'empty':
        if len(dq) == 0:
            print(1)
        else:
            print(0)
    elif c[0] == 'front':
        if len(dq) != 0:
            print(dq[0])
        else:
            print(-1)
    else:
        if len(dq) != 0:
            print(dq[-1])
        else:
            print(-1)