A,B=input().split()
k=0
for i in range(0,min(len(A),len(B))):
    k+=(int(A[len(A)-i-1])+int(B[len(B)-i-1]))*(10**i)
if len(A)>len(B):
    k+=int(A[:len(A)-len(B)])*(10**(len(B)))
elif len(B)>len(A):
    k+=int(B[:len(B)-len(A)])*(10**(len(A)))

print(k)   