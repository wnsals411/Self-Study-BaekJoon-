def sosu(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i-1] == True:           # i가 소수인 경우
            for j in range(i*2-1, n, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n+1) if sieve[i-1] == True]

T = int(input())
for i in range(T):
    n = int(input())
    partition = []
    sosu_list = sosu(n)

    for a in sosu_list[:len(sosu_list)//2+1]:
        for b in sosu_list[len(sosu_list)//2:]:
            if a+b == n:
                partition.append([a, b])
                break

    print(len(sosu_list)//2+1)