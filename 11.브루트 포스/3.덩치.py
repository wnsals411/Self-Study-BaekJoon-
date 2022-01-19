N = int(input())
wh_list = []
rank = []

for i in range(N):    
    x, y = map(int, input().split())
    wh_list.append([x, y])

for i in range(len(wh_list)):
    count = 1 # 1등부터 시작하기 때문에
    for k in range(len(wh_list)):
        if wh_list[i][0] < wh_list[k][0] and wh_list[i][1] < wh_list[k][1]:
            count += 1
    rank.append(count)
            
for e in rank:
    print(e, end=' ')        

print()