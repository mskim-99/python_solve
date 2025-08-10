T = int(input())

for tc in range(T):
    calendar = list(map(str, input()))

    year = ''.join(calendar[:4])
    month = ''.join(calendar[4:6])
    day = ''.join(calendar[6:])

    if int(month) in [1, 3, 5, 7, 8, 10, 12]:
        if 1 <= int(day) <= 31:
            print(f"#{tc + 1} {year}/{month}/{day}")
        else:
            print(f"#{tc + 1} -1")
    elif int(month) in [4, 6, 9, 11]:
        if 1 <= int(day) <= 30:
            print(f"#{tc + 1} {year}/{month}/{day}")
        else:
            print(f"#{tc + 1} -1")
    elif int(month) == 2:
        if 1 <= int(day) <= 28:
            print(f"#{tc + 1} {year}/{month}/{day}")
        else:
            print(f"#{tc + 1} -1")
    else:
        print(f"#{tc + 1} -1")