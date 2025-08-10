T = int(input())

dr_1 = [0, 1, 0, -1]    # 우하좌상 직선 델타
dc_1 = [1, 0, -1, 0]

dr_2 = [1, 1, -1, -1]   # 5시부터 대각선 델타
dc_2 = [1, -1, -1, 1]

for tc in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)] # NxN 배열 생성

    max_flies = 0
    for i in range(N):
        for j in range(N):

            catch_flies_beeline = arr[i][j]   # 직선 잡은 파리의 중심 값
            catch_flies_diagonal = arr[i][j]   # 대각선 잡은 파리의 중심값
            
            for k in range(4):
                for l in range(1, M):
                    nr_1 = i + (dr_1[k] * l)  # 우하 좌상 직선
                    nc_1 = j + (dc_1[k] * l)

                    if 0 <= nr_1 < N and 0 <= nc_1 < N: # 배열 범위 내 이면 더하기
                        catch_flies_beeline += arr[nr_1][nc_1]
                    else:
                        catch_flies_beeline += 0
                
                for l in range(1, M):
                    nr_2 = i + (dr_2[k] * l)  # 5시 부터 대각선
                    nc_2 = j + (dc_2[k] * l)

                    if 0 <= nr_2 < N and 0 <= nc_2 < N: # 배열 범위 내 이면 더하기
                        catch_flies_diagonal += arr[nr_2][nc_2]
                    else:
                        catch_flies_diagonal += 0
            
            max_flies = max(max_flies, catch_flies_beeline, catch_flies_diagonal)
    
    print(f"#{tc + 1} {max_flies}")