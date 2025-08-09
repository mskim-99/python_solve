alphabets = list(map(str, input()))

for i in alphabets: # 대문자 아스키 코드 값
    print((ord(i) - 64), end=" ")
print()