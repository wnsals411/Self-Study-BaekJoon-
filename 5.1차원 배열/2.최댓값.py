A = []
for i in range(9):
    A.append(int(input()))
print(max(A))
for i in range(len(A)):
    if A[i] == max(A):
        print(i+1)