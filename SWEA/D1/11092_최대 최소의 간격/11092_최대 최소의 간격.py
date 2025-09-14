T = int(input())

for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    min_value_index = arr.index(min(arr))
    max_value = max(arr)
    max_vlaue_index = 0 # 최대값의 인덱스

    # 배열의 뒤부터 순회하면서 최대값 인덱스 탐색
    for i in range(len(arr)-1, -1, -1):
        if arr[i] == max_value:
            max_vlaue_index = i
            break
    
    # 절대값 거리 저장
    result = abs(max_vlaue_index - min_value_index)

    print(f"#{tc+1} {result}")