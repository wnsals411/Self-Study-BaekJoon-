A, B, C = map(int, input().split())

try:
    r = A/(C-B)

    if r >= 0:
        print(int(r+1))
    else:
        print(-1)

except ZeroDivisionError:
    print(-1)
