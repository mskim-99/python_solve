# G : 이동 가능한 땅
# T : 이동 불가능한 나무가 위치
# X : 현재 RC카의 위치
# Y : RC카 도착 지점

# 커맨드 : 
#   - A : 앞으로 이동 (필드를 벗어나거나 나무면 아무일 X)
#   - L : 현재 바라보는 방향에서 왼쪽으로 90도 회전
#   - R : 현재 바라보는 방향에서 오른쪽으로 90도 회전

# 커맨드 종료시 목적지에 도달 했는지 확인

# 1. 테스트 케이스
# 2. 필드의 크기 N
# 3. 필드의 정보
# 4. 조종을 한 횟수 Q
# 5. Q개의 줄에는 커맨드의 길이 C와 커맨드가 주어짐

# import sys
# sys.stdin = open("sample_input.txt")

# RC카의 위치를 찾는 함수
def find_RC(field):
    for i in range(N):
        for j in range(N):
            if field[i][j] == 'X':
                return (i, j)

# RC카를 이동 시키는 함수
def move_RC(start, field, command):
    global finish   # 결과를 받을 배열
    start_1, start_2 = start    # 시작 지점 x, y

    # 커맨드 꺼내기
    for _, cmd in command:
        x, y = start_1, start_2 # 시작 위치 할당
        car = 0 # 상0 우1 하2 좌3

        for c in cmd:
            if c == 'R':    # R 이라면 우측으로 회전
                car = (car + 1) % 4
            elif c == 'L':  # L 이라면 좌측으로 회전
                car = (car + 3) % 4
            elif c == 'A':  # A라면 회전 값으로 이동
                nx, ny = x + dr[car], y + dc[car]
                if 0 <= nx < N and 0 <= ny < N and field[nx][ny] != 'T':
                    x, y = nx, ny   # 최종 위치 갱신
        
        if field[x][y] == 'Y':  # 커맨드 종료시 현재 위치가 Y라면
            finish.append(1)
        else:
            finish.append(0)



T = int(input())    # test case
dr = [-1, 0, 1, 0]  # 상우하좌
dc = [0, 1, 0, -1]

for tc in range(T):
    N = int(input())    # 필드의 크기
    field = [list(input().strip()) for _ in range(N)]
    Q = int(input())    # 커맨드 길이
    command = [input().split() for _ in range(Q)]

    start = find_RC(field)  # 시작점 찾기
    finish = []             # 결과를 받을 배열
    move_RC(start, field, command)  # 커맨드로 RC카 이동

    print(f"#{tc+1}", end=' ')  # 결과값 출력
    for i in range(Q):
        print(finish[i], end=' ')
    print()