N = int(input())

number = list(map(int, input().split()))
number.sort()

result = N // 2

print(number[result])