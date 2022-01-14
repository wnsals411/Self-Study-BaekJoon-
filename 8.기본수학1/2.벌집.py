N = int(input())

N = N-1 # 첫방 제외
count = 1

for i in range(1, 1000000000):
    if N == 0:
        break
    elif N // (6*i) > 0:
        N -= (6*i)
        count += 1
    else:
        count += 1
        break

print(count)