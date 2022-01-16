def sosu(a):
    if a < 2:
        return 0
    else:
        for i in range(2, a):
            if a % i == 0:
                return 0
                break
        return 1

        

N = int(input())
ls = list(map(int, input().split()))

count = 0

for e in ls:
    count += sosu(e)

print(count)
