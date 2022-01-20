def check_count(n, m):
    count = 0
    check_list = []

    for i in range(8):
        tmp_list = []
        for k in range(8):
            tmp_list.append(input_list[n+i][m+k])
        check_list.append(tmp_list)

    if check_list[0][0] == 'W':
        for i in range(8):
            for k in range(8):
                if check_list[i][k] != chess_list[i][k]:
                    count += 1
    else:
        for i in range(8):
            for k in range(8):
                if check_list[i][k] == chess_list[i][k]:
                    count += 1

    if count > 32:
        count = 64 - count

    return count

N, M = map(int, input().split())

input_list = []
chess_list = []
count_list = []
for _ in range(4):
    chess_list.append(list('WBWBWBWB'))
    chess_list.append(list('BWBWBWBW'))

for _ in range(N):
    input_list.append(list(input()))

for i in range(N-7):
    for k in range(M-7):
        count_list.append(check_count(i, k))

print(min(count_list))