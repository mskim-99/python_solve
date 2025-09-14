
T = 10  # test case

for tc in range(T):
    N = int(input())    # 건물의 개수
    box = list(map(int, input().split()))   # 각 건물의 높이

    count = 0   # 조망권 확보된 세대 수
    for i in range(2, N-2):
        value = max(box[i-2], box[i-1], box[i+1], box[i+2]) # 양옆에 2칸씩 최대값 구하기
        if box[i] > value:  # 만약 현재 빌딩이 가장 높다면
            count += box[i] - value # 양 옆 2칸 최대값을 뺀 값을 조망권에 추가

    print(f"#{tc+1} {count}")