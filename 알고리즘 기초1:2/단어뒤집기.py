import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    s = input().rstrip().split()
    
    for w in s:
        for i in range(len(w)-1, -1, -1):
            print(w[i], end='')
        print(' ', end='')
    print()