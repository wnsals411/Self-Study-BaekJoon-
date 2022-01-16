def sosu(a):
    if a < 2:
        return 0
    else:
        for i in range(2, a):
            if a % i == 0:
                return 0
                break
        return 1

M = int(input())
N = int(input())

sosu_ls = []

for i in range(M, N+1):
    if sosu(i) == 1:
        sosu_ls.append(i)

if len(sosu_ls) == 0:
    print(-1)
else:    
    print(sum(sosu_ls))
    print(min(sosu_ls))