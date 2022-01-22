N = int(input())
member_ls = []

for _ in range(N):
    age, name = input().split()
    member_ls.append([int(age), name])

member_ls.sort(key=lambda x:x[0])

for e in member_ls:
    print(e[0], e[1])