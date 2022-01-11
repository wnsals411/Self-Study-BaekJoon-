N = int(input())
score = 0

for i in range(N):
    line = input()
    TC = []
    for a in line:
        TC.append(a)
    
    for k in range(len(TC)):
        if TC[k] == 'O':
            score += 1
            TC[k] = score
        else:
            score = 0
            TC[k] = score
    print(sum(TC))
    score = 0