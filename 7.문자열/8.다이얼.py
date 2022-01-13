dials_num = [3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,8,9,9,9,10,10,10,10]

s = input().upper()
sum = 0

for e in s:
    sum += dials_num[ord(e)-ord('A')]

print(sum)