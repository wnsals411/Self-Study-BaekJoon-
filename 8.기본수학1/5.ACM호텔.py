import math
T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())

    # 층을 구하는 방식
    # 방문객을 층으로 나눈 나머지 (단, 나머지가 0인 경우 최상층(=건물높이))
    # 방을 구하는 방식
    # 방문객을 층으로 나눈 값을 올림
    room = math.ceil(N/H)
    floor = N%H
    if floor == 0:
        floor = H
    if room < 10:
        print('%d0%d'%(floor, room))
    else:
        print('%d%d'%(floor, room))