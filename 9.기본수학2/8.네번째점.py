a1_x, a1_y = map(int, input().split())
a2_x, a2_y = map(int, input().split())
a3_x, a3_y = map(int, input().split())

x = [a1_x, a2_x, a3_x]
y = [a1_y, a2_y, a3_y]

for e in set(x):
    if x.count(e) == 1:
        print(e, end=' ')

for e in set(y):
    if y.count(e) == 1:
        print(e)