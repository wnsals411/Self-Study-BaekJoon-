N = int(input())
soinsu_ls = []
for i in range(2, N+1):
    while True:
        if N % i == 0:
            soinsu_ls.append(i)
            N = N // i
        else:
            break

for e in soinsu_ls:
    print(e)