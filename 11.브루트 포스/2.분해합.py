# n의 각 자리수의 합을 반환하는 함수
def n_sum(n):
    s = 0
    for e in str(n):
        s += int(e)

    return s

N = int(input())

for M in range(N):
    if M + n_sum(M) == N:
        print(M)
        break
    elif M == N-1:
        print(0)
        break