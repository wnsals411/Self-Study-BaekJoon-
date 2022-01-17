while True:
    A, B, C = map(int, input().split())
    if A == 0 and B == 0 and C == 0:
        break
    r = [A**2, B**2, C**2]
    tmp = max(r)
    r.remove(tmp)
    if tmp == sum(r):
        print('right')
    else:
        print('wrong')