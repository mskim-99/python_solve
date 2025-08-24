T = 10
result = []                                             # 최대 높이 - 최소 높이 값을 받을 배열

for tc in range(10):
    dump = int(input())

    box = list(map(int, input().split()))

    for k in range(dump):                               # 입력받은 dump의 수 만큼 반복
        for i in range(99, 0, -1):                      # 입력 받은 100상자 버블정렬
            for j in range(i):
                if box[j] > box[j+1]:
                    box[j], box[j+1] = box[j+1], box[j]
        box[-1] -= 1                                    # 가장 큰 값을 -1, 가장 작은 값을 +1 실행
        box[0] += 1
        if k == (dump - 1):                             # 만약 dump 즉, 마지막 반복 이라면 버블 정렬 다시 실행
            for i in range(99, 0, -1):
                for j in range(i):
                    if box[j] > box[j+1]:
                        box[j], box[j+1] = box[j+1], box[j]

    result.append(box[-1] - box[0])                     # 버블 정렬 된 값에서 최대 값과 최소 값 차이 배열에 추가

for l in range(10):
    print(f"#{l+1} {result[l]}")