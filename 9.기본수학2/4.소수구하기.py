def root(a):
    return a ** 0.5

M, N = map(int, input().split())

true_table = [True] * N

for i in range(2, int(root(N))+1):
    if true_table[i-1] == True:
        for j in range(i*2-1, N, i):
            true_table[j] = False

re = [i for i in range(2, N+1) if true_table[i-1] == True and i >= M]

for e in re:
    print(e)