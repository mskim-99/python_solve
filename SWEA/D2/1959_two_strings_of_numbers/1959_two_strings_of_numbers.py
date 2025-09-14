T = int(input())    # 테스트 케이수 수 입력받는 변수

for tc in range(T):
    max_value = 0   # 최대값 저장 변수
    N, M = map(int, input().split())

    A_arr = list(map(int, input().split()))
    B_arr = list(map(int, input().split()))

    # A_arr, B_arr 둘 중 어느 배열의 길이가
    # 길지 모르니 A가 더 크면 스왑
    if len(A_arr) > len(B_arr):
        A_arr, B_arr = B_arr, A_arr

    # 긴쪽 - 짧은쪽 만큼 반복 진행
    for i in range((max(N, M) - min(N, M)) + 1):
        result = 0  # 결과 합산을 받을 변수
        for j in range(min(N, M)):
            # 한 칸씩 이동하면서 마주보는 부분 계산
            result += A_arr[j] * B_arr[i+j]
        max_value = max(max_value, result)

    print(f"#{tc + 1} {max_value}")


# 8/31 두번 째 풀이
# 길이 N인 배열 Ai
# 길이 M인 배열 Bj

# 각 배열을 자유롭게 움직여 숫자를 마주보는 위치 변경 가능
# 더 긴쪽의 양 끝을 벗어나면 안된다.

# 3 <= N <= 20
# 3 <= M <= 20

# T = int(input())

# for tc in range(T):
#     N, M = map(int, input().split())
#     Ai = list(map(int, input().split()))
#     Bj = list(map(int, input().split()))

#     if N > M:   # N이 항상 더 작다는 가정
#         Ai, Bj = Bj, Ai
#         N, M = M, N

#     result = []
#     for i in range(M-N+1):
#         count = 0
#         for j in range(N):
#             count += (Ai[j] * Bj[j+i])
#         result.append(count)

#     print(f"#{tc+1} {max(result)}")