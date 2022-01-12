N = int(input())
hansoo = []

def makelist_hansoo(n):
    global hansoo
    for i in range(1, N+1):
        if i < 100:
            hansoo.append(i)
        elif i >= 100 and i < 1000:
            a = list(str(i))
            if int(a[1]) - int(a[0]) == int(a[2]) - int(a[1]):
                hansoo.append(i)
        else:
            pass
    return hansoo

makelist_hansoo(N)

print(len(hansoo))