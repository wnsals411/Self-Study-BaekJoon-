import string

input = input().upper()
U_a_ls = list(string.ascii_uppercase)
count_ls = []

for element in U_a_ls:
    count_ls.append(input.count(element))

if count_ls.count(max(count_ls)) != 1:
    print('?')
else:
    print(U_a_ls[count_ls.index(max(count_ls))])
