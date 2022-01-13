T = int(input())

for i in range(T):
    R, S = input().split()
    for k in list(S):
        print(int(R) * k, end='')
    print()