def dfs(cnt, result):
    global min_value
    # 가지 치기
    if result >= B:
        min_value = min(min_value, result - B)
        return

    # 종료 조건
    if cnt == N:
        return

    # 분기점
    if min_value == 0:
        return 
    
    # 부분집합에 포함시키는 경우
    dfs(cnt + 1, result + arr[cnt])
    
    # 부분 집합에 포함시키지 않는 경우
    dfs(cnt + 1, result)

T = int(input()) #test case

for tc in range(T):
    # N : 점원 수, B : 선반 높이
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    min_value = 9999999
    
    dfs(0, 0)
    print(f"#{tc+1} {min_value}")
