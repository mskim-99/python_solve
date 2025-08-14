T = int(input()) # 입력 테스트 케이스 수

for tc in range(T):
    N = int(input())    # NxN 배열
    result_1 = []   # 최종 결과 값을 저장할 배열
    result_2 = []
    result_3 = []
    arr = [list(input().split()) for _ in range(N)]
    for i in range(N):
        value_1 = []    # 90도, 180도, 270도 회전한 데이터 값 저장
        for k in range(N - 1, -1, -1):
            value_1.append(arr[k][i])
        result_1.append(''.join(value_1))

    for j in range(N-1, -1, -1):
        value_2 = []    # 90도, 180도, 270도 회전한 데이터 값 저장
        value_3 = []    # 90도, 180도, 270도 회전한 데이터 값 저장

        for l in range(N-1, -1, -1):
            value_2.append(arr[j][l])
        result_2.append(''.join(value_2))
        for m in range(N):
            value_3.append(arr[m][j])
        result_3.append(''.join(value_3))

    print(f"#{tc + 1}")
    for i in range(N):
        print(result_1[i], result_2[i], result_3[i])