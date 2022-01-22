# N = int(input())
# ls = []

# for _ in range(N):
#     ls.append(int(input()))

# ls.sort()

# for e in ls:
#     print(e)

N = int(input())
ls = []

for _ in range(N):
    ls.append(int(input()))
    
    if len(ls) >= 2:
        for i in range(len(ls)-1, 0, -1):
            if ls[i] < ls[i-1]:
                ls[i], ls[i-1] = ls[i-1], ls[i]

for e in ls:
    print(e)