import string

S = input()

alphabet = list(string.ascii_lowercase)

for element in alphabet:
    print(S.find(element), end=' ')