A, B = map(int, input().split())
a = ''
b = ''

def change(n):
    r = []
    for i in range(len(list(str(n)))-1, -1, -1): # '4''3''7'
        r.append(str(n)[i])
    return r


for element in change(A):
    a += element

for element in change(B):
    b += element


if int(a) > int(b):
    print(int(a))
else:
    print(int(b))