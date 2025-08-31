# 원본 문서는 너비가 10인 여러줄 문자열
# 문자열은 마지막 줄을 제외하고 공백없이 알파벳
# 마지막 줄은 왼쪽부터 채워져 있다

# ex. A 5 == AAAAA

# A 10
# B 7
# C 5

# AAAAAAAAAA
# BBBBBBBCCC
# CC

# 제약 사항
# 1. 알파벳과 숫자 쌍의 개수 N은 1 <= N <= 10
# 2. 알파벳은 A-Z Ci
# 3. 알파벳의 연속된 수 Ki. 1 <= Ki <= 20
# 4. 원본 문서의 너비는 10 고정

T = int(input())

for tc in range(T):
    N = int(input())
    alphabet = [list(map(str, input().split())) for _ in range(N)]

    print(f"#{tc+1}")
    print_count = 0 # 몇 번 출력했는지 확인 하는 변수
    for Ci, Ki in alphabet:
        count = int(Ki) # 각 Ci를 몇 번 출력한 것인지
        for i in range(count):
            print(Ci, end='')  # Ki 만큼 붙여서 출력
            print_count += 1   # 몇 번 출력했는지 체크
            if print_count % 10 == 0:   # 만약 너비 10만큼 출력했다면
                print()                 # 다음 줄 부터 출력 
    print()