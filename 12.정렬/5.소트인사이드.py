N = int(input())
ls = list(str(N))

ls.sort(reverse=True)

for e in ls:
    print(int(e), end='')
print()