# import sys
# sys.stdin = open("input.txt", "r")


# I(삽입) x, y, s : x번째 다음에 y개의 암호문 s들을 삽입
# D(삭제) x, y : x번째 암호문 다음에 y개의 암호문을 삭제
# A(추가) y, s : 맨 뒤에 y개의 암호문 s를 붙인다.

# 처음 10개의 암호문 출력

# 2000 <= N <= 4000     N : 원본 암호문 개수
# 원본 암호문 배열
# 250 <= M <= 500       M : 명령어 개수
# 명령어

T = 10

for tc in range(T):
    N = int(input())    # 원본 암호문 개수
    arr = list(map(int, input().split()))   # 원본 암호문 배열
    M = int(input())    # 명령어 개수
    command = list(map(str, input().split()))   # 명령어 배열

    x = 0 # while 문의 인덱스 조정
    idx = 0 # 삽입, 삭제 인덱스
    cnt = 0 # 반복 횟수
    while x < len(command):
        idx, cnt = int(command[x + 1]), int(command[x + 2])
        if command[x] == 'I':   # I일 경우 삽입
            x += 3
            for i in range(cnt):
                arr.insert(idx+i, int(command[i+x]))
            x += cnt
        elif command[x] == 'D': # D일 경우 삭제
            x += 3
            for i in range(cnt):
                arr.pop(idx)
        elif command[x] == 'A': # A일 경우 마지막에 추가
            x += 2
            for i in range(idx):
                arr.append(int(command[i+x]))
            x += idx

    print(f"#{tc+1} ", end='')
    for i in range(10):
        print(arr[i], end=' ')
    print()