N, M = map(int, input().split())
card_list = list(map(int, input().split()))
sum_list = []

for a in range(len(card_list)):
    for b in range(a+1, len(card_list)):
        for c in range(b+1, len(card_list)):
            sum_list.append(card_list[a] + card_list[b] + card_list[c])

sum_list.sort(reverse=True)

for e in sum_list:
    if e <= M:
        print(e)
        break