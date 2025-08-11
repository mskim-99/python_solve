
T = int(input())

for tc in range(T):
    arr1 = list(map(str, input()))
    arr2 = list(map(str, input()))

    set(arr1)   # 중복 제거
    list(arr1)

    result = 0  # 최종 결과를 받을 변수
    for i in arr1:  # arr1 순회하며 값 추출
        count = 0
        for j in arr2:  # arr2 순회하며 값 추출
            if i == j:  # arr1과 arr2의 원소가 같다면
                count += 1  # count 1 증가
                continue    # 종료되지 않게 반복
        if count > result:  # 최종 결과보다 count가 크면 갱신
            result = count

    print(f"#{tc + 1} {result}")