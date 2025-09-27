import sys
sys.stdin = open("sample_input.txt")

# 출발지 인덱스를 찾는 함수
def find_start(maze):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return (i, j)

# DFS 함수
def dfs(maze, start):
    global result
    x, y = start
    visited[x][y] = 1   # 시작 지점 방문 처리

    # 종료 조건
    if maze[x][y] == 3:
        result = 1
        return


    for i in range(4):
        nr, nc = dr[i] + x, dc[i] + y
        if 0 <= nr < N and 0 <= nc < N and maze[nr][nc] != 1 and not visited[nr][nc]:
            dfs(maze, (nr, nc)) # 재귀
    
    visited[x][y] = 0
    return


T = int(input()) # test case
dr = [0, 1, 0, -1] # 우하좌상
dc = [1, 0, -1, 0]

for tc in range(T):
    N = int(input())    # 미로 크기
    maze = [list(map(int, input())) for _ in range(N)]

    visited = [[0] * N for _ in range(N)]
    result = 0
    start = find_start(maze)
    dfs(maze, start)

    print(f"#{tc+1} {result}")