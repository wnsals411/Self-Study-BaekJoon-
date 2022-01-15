import sys
n = int(sys.stdin.readline().rstrip())

cases = []
for i in range(n):
    cases.append(list(map(int, sys.stdin.readline().rstrip().split())))

for x, y in cases:
    right_n = 1
    left_n = 0
    distance = y - x
    right_distance = 0
    left_distance = 0
    flag = 1
    while True:
        right_distance = right_n*(right_n+1)/2
        left_distance = left_n*(left_n+1)/2
        if distance-(right_distance+left_distance) <= 0:
            print(right_n+left_n)
            break

        if flag == 1:
            left_n += 1
            flag = 0
        else:
            right_n += 1
            flag = 1