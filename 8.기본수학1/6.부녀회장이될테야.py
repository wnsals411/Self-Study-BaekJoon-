# 시간초과 이슈로 pypy3로 제출해야 통과
def solve(floor, room):
    if room == 1:
        return 1
    elif floor == 0:
        return room
    else:
        return (solve(floor-1, room) + solve(floor, room-1))

T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())

    print(solve(k, n))