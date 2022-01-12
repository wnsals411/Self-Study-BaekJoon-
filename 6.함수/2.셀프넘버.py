def sum(n):
    sum = 0
    for i in str(n):
        sum += int(i)    
    return sum

def solve(n):
    r = n + sum(n)
    return r


a = list(range(1, 10001))

for i in range(1, 10001):
    if solve(i) in a:
        a.remove(solve(i))

for k in a:
    print(k)