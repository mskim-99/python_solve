# # 연속된 N일 동안의 매매가 예측
# # 하루에 최대 1만큼 구입 가능
# # 판매는 개수 제한 X

# # ex. 3일 동안 매매가가 1, 2, 3 이라면
# # 처음 두 날에 원료를 구매하여 마지막에 팔면 3의 이득

# # 1. 테이스 케이스 수
# # 2. 각 케이스 별 N
# # 3. 날짜 별 N개의 매매가
# # 매매가는 10,000 이하

# T = int(input())

# for tc in range(T):
#     N = int(input())
#     price = list(map(int, input().split(' ')))
    
#     my_queue = []
#     copy_price = price.copy() # 매매가를 그대로 복사한 배열
#     result = 0
#     for i in range(len(price)-1):
#         one, two = price[i], price[i+1]
#         if one <= two:  # 첫번째 매매가가 두번째 매매가 보다 작다면 스택에 삽입
#             my_queue.append(one)
#             print(my_queue)
#         else :
#             print(my_queue)
#             queue_length = len(my_queue)
#             result += one * queue_length
#             while my_queue:
#                 result -= my_queue.pop()
    
#     print(f"#{tc+1} {result}")