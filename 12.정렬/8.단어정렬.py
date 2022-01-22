N = int(input())
word_ls = []
for _ in range(N):
    word = input()
    if word in word_ls:
        pass
    else:
        word_ls.append(word)

word_ls.sort()
word_ls.sort(key=lambda x:len(x))

for e in word_ls:
    print(e)