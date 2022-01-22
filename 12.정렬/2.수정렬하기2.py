import sys

N = int(sys.stdin.readline())
ls = []

for _ in range(N):
    ls.append(int(sys.stdin.readline()))

ls.sort()

for e in ls:
    print(e)