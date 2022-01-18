############################################################
'''
하노이의 탑은 세 개의 장대(A, B, C)가 있고 n개의 원판을
A에서 C로 B를 경유하여 옮기기 위해
1. A -> B로 n-1개 이동
2. A -> C로 n번째 원판 이동
3. B -> C로 n-1개 이동
의 과정을 거친다
'''
############################################################
N = int(input())
count = 0
process = []
def hanoi(N, start, to, via): # N개의 원판을 start -> to 까지 경유지 via
    global count
    global process
    if N == 1:
        count += 1
        process.append([start, to])
    else:
        hanoi(N-1, start, via, to)
        count += 1
        process.append([start, to])
        hanoi(N-1, via, to, start)

    return count

# 출력형식 맞추기
print(hanoi(N, 1, 3, 2))
for i in process:
    for e in i:
        print(e, end=' ')
    print()