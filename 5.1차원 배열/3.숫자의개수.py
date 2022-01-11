A = int(input())
B = int(input())
C = int(input())

str = str(A * B * C)
list = []

for i in range(len(str)):
    list.append(int(str[i]))

for i in range(10):
    print(list.count(i))