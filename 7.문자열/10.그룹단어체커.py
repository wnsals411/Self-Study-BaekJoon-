N = int(input())
count = 0

for i in range(N):
    word = input()

    if len(word) in (1, 2): # 길이가 3 이상일 때만 연속이 끊어짐
        count += 1
    else:
        for k in range(len(word)-1): 
            if word[k] == word[k+1]: # 앞문자와 뒷문자가 같을 경우
                pass
            else:
                if word[k] in word[k+1:]: # 그룹 단어가 아닌 경우
                    count -= 1 # for문 밖에 count += 1이 있기 때문
                    break # for문 강제 탈출
                else:
                    pass
        count += 1 # for문 탈출(그룹 단어인 경우)

print(count)