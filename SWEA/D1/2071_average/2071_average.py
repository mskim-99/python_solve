T = int(input())

for tc in range(T):
    number = list(map(int, input().split()))
    sum_number = sum(number) // len(number)

    if (sum(number) / len(number)) % sum_number >= 0.5:
        sum_number = (sum(number) // len(number)) + 1

    print(f"#{tc + 1} {sum_number}")