# 영어 대문자 A-Z, 소문자 a-z
# 숫자 0-9
# 글자를 수평으로 붙여서 글자를 만듦

# 단어들의 글자 개수는 다를 수 있다
# 단어를 세로로 읽으려 한다.
# 세로 마다 같은 인덱스의 글자를 읽는다.
# 만약 글자가 없다면 다음 인덱스의 글자를 읽는다.
# 세로로 읽은 순서를 공백없이 출력

# 테이스 케이스는 총 5줄
# 각 줄에 길이 1이상 15이하 문자열이 주어진다.

T = int(input())

for tc in range(T):
    word = [list(map(str, input())) for _ in range(5)]
    length = max(len(w) for w in word)  # 가장 길이가 긴 행 찾기
    print(f"#{tc+1}", end=' ')
    for i in range(length):
        for j in range(5):
            try:
                print(word[j][i], end='')
            except IndexError: # 예외가 발생하면 반복문 건너뛰기
                continue
    print()
