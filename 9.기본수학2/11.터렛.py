T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    d = ((x2-x1)**2 + (y2-y1)**2)**0.5 # 두 좌표 간 거리

    #print(d)
    if d != 0 and d > abs(r1 - r2) and d < r1 + r2:
        print(2)
        #pass
        # 두 점에서 만나는 경우
    elif d != 0 and (d == r1 + r2 or d == abs(r1 - r2)):
        print(1)
        #pass
        # 한 점에서 만나는 경우
    elif (d == 0 and abs(r1 - r2) != 0) or (d != 0 and d > r1 + r2):
        print(0)
        # pass
        # 한 점에서도 안 만날 경우
    else:
        print(-1)
        # 무수히 많은 점에서 만날 경우
        #pass