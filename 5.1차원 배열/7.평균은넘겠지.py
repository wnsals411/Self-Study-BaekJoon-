import sys 
C = int(sys.stdin.readline())
for i in range(C):
    line = list(map(int, sys.stdin.readline().split()))
    N = line[0]
    score = line[1:]
    count = 0
    for a in score:
        if a > sum(score) / N:
            count += 1
    
    print("%.3f" % round(count/N*100, 3), end='')
    print('%')