N = int(input())

q_5 = 0
q_3 = 0
r = 0

for i in range(N//5, -1, -1):
   r = N - (5*i)
   if r % 3 == 0:
        q_5 = i
        q_3 = r // 3
        break

if q_5 == 0 and q_3 == 0:
    print(-1)
else:
    print(q_5 + q_3)