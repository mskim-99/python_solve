T = int(input())

for tc in range(T):
    number = list(map(int, input().split()))

    print(f"#{tc + 1} {max(number)}")