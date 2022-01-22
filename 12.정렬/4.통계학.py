import sys
n = int(sys.stdin.readline())
num = [int(sys.stdin.readline()) for _ in range(n)]
num.sort()

print(round(sum(num)/n))

print(num[(n-1)//2])

p=-4001
count = 0 #현재 숫자가 등장한 횟수
best = 1 #최빈값의 등장 횟수
mode = [] #최빈값 목록

for i in num:
    if i == p:
        count += 1
    else:
        count = 1

    if count == best:
        mode.append(i)
    elif count > best:
        mode = [i]
        best = count
    
    p = i

try:
    print(mode[1])
except:
    print(mode[0])

print(num[-1]-num[0])