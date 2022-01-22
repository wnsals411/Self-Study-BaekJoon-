import sys

N = int(sys.stdin.readline())
ls = list(map(int, sys.stdin.readline().split()))
sort_ls = sorted(set(ls))

ls_dict={i:v for v,i in enumerate(sort_ls)}
print(ls)
print(ls_dict)

# for i in ls:
#     print(ls_dict[i], end=' ')
# print()