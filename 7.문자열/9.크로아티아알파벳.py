before = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
after = ['č', 'ć', '3', 'đ', '1', '2', 'š', 'ž'] # 1 - lj, 2 - nj 3 - dž

input = input()

for i in range(len(before)):
    input = input.replace(before[i], after[i])

print(len(input))