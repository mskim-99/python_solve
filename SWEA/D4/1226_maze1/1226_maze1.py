from collections import deque
# import sys

# sys.stdin = open("input.txt")


# 시작점을 찾는 함수
def find_start(maze):
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2: # 시작점을 찾으면
                return (i, j)   # 시작점 좌표 리턴
    return None

def bfs(maze, start):   # 미로와 시작점
    visited = [[False] * 16 for _ in range(16)] # 방문 처리할 배열
    queue = deque([start]) #시작점을 넣은 덱 생성
    visited[start[0]][start[1]] = True  # 시작점은 방문 처리

    while queue:    # 큐가 비어 있지 않으면 반복
        # 시작점 꺼내기
        x, y = queue.popleft()

        # 만약 골이라면
        if maze[x][y] == 3:
            return 1
        
        # 인접 칸들 방문
        for i in range(4):  # 델타 검색
            di, dj = x + dr[i], y + dc[i]

            # di, dj가 범위 내 이고, 벽이 아닌 경우, 방문하지 않은 경우
            if 0 <= di < 16 and 0 <= dj < 16 and maze[di][dj] != 1 and not visited[di][dj]:
                visited[di][dj] = True  # 방문 처리
                queue.append((di, dj))  # 현재 위치 삽입

    return 0    # 도착점을 찾지 못하면 0 리턴


T = 10  # test case
dr = [0, 1, 0, -1]  # 우하좌상
dc = [1, 0, -1, 0]

for tc in range(T):
    test_case = int(input())
    maze = [list(map(int, input())) for _ in range(16)]

    start = find_start(maze)    # 시작점
    goal = bfs(maze, start)     # 골인

    print(f"#{test_case} {goal}")