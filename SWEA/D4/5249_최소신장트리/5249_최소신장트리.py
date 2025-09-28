# import sys
# sys.stdin = open("sample_input.txt")

from heapq import heappush, heappop

def prim(start_node):
    pq = [(0, start_node)]  # 가중치, 시작노드
    min_value = 0
    MST = [0] * (V + 1) # visited 역할

    while pq:   # heap큐가 비어있지 않으면
        weight, node = heappop(pq)

        if MST[node]:   # 이미 방문했다면
            continue
        
        MST[node] = 1   # 방문 처리
        min_value += weight # 가중치 추가

        for next_node in range(V+1):
            # 가중치가 없는 경우
            if graph[node][next_node] == 0:
                continue
        
            heappush(pq, (graph[node][next_node], next_node))

    return min_value

T = int(input())

for tc in range(T):
    V, E = map(int, input().split())
    graph = [[0] * (V + 1) for _ in range(V + 1)]

    for i in range(E):
        start, end, weight = map(int, input().split())
        graph[start][end] = weight
        graph[end][start] = weight
    
    result = prim(0)
    print(f"#{tc+1} {result}")