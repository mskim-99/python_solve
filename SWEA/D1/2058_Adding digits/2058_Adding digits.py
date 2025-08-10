N = int(input())
sum_number = 0

for i in range(4):
    sum_number += N % 10
    N = N // 10

print(sum_number)