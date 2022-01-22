N = int(input())
ls = []

for _ in range(N):
    x, y = map(int, input().split())
    ls.append([x, y])

ls.sort()
ls.sort(key=lambda x: x[1])

for e in ls:
    print(e[0], e[1])