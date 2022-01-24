import sys
input = sys.stdin.readline
stack = []
N = int(input())

for _ in range(N):
    cmd = input().strip()
    if 'push' in cmd:
        stack.append(int(cmd.split()[1]))
    elif cmd == 'pop':
        try:
            print(stack.pop())
        except IndexError:
            print(-1)
    elif cmd == 'size':
        print(len(stack))
    elif cmd == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif cmd == 'top':
        try:
            print(stack[-1])
        except IndexError:
            print(-1)