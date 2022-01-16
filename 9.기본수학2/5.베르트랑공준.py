def root(a):
    return a ** 0.5

while True:
    N = int(input())
    n = 2 * N
    if N == 0:
        break
    
    true_table = [True] * n

    for i in range(2, int(root(n))+1):
        if true_table[i-1] == True:
            for j in range(i*2-1, n, i):
                true_table[j] = False

    re = [i for i in range(2, n+1) if true_table[i-1] == True and i > N]

    print(len(re))