N, X = map(int, input().split())
A = list(map(int, input().split()))

for element in A:
    if element < X:
        print(element, end=' ')