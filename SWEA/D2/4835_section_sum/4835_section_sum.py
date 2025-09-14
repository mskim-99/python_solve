T = int(input())

for tc in range(T):
    # N : 정수의 개수, M : 구간의 개수
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    section_sum = []    # 각 구간합을 저장할 배열
    for i in range(N - M + 1):
        section_sum.append(sum(arr[i:i+M]))
    
    section_sum.sort()  # 배열 정렬
    result = section_sum[-1] - section_sum[0]

    print(f"#{tc+1} {result}")