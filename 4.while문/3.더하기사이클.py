import sys

N = int(sys.stdin.readline())
# N//10 (십의자리)
# N%10  (일의자리)
res = N
count = 0

while True:
    res = (res%10)*10 + (((res//10) + (res%10))%10)
    count += 1
    if res == N:
        break
    
print(count)