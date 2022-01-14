X = int(input())

sum = 0
tear = 0

for i in range(1, 10000):
    if sum > 10000000:
        break
    else:
        sum += i
        tear += 1
        if X <= sum:
            break

if tear%2 == 0:
    A = tear - (sum - X)
    B = 1 + (sum - X)

else:
    A = 1 + (sum - X)
    B = tear - (sum - X)

print('%d/%d'%(A,B))