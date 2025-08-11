
T = int(input())

for tc in range(T):
    str1 = list(input())    # 첫 번째 문자열
    str2 = list(input())    # 두 번째 문자열
    N = len(str1)

    result = 0  # 최종 결과 변수
    count = 0   # 문자열이 몇 번 존재 하는지 셀 변수
    for i in range(len(str2)):
        str1_value = ''.join(str1[:])   # 하나의 문자열로 변환
        str2_value = ''.join(str2[i : i + N])   # 두 번째 문자열 순회

        if str1_value == str2_value:    # 찾는 문자열이 존재하면
            count += 1

    if count >= 1:  # 1개 이상 있다면 1 반환
        result = 1  # 없다면 0 반환
    else:
        result = 0

    print(f"#{tc + 1} {result}")