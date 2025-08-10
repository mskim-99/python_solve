def solution(n, arr1, arr2):
    arr_1 = []
    arr_2 = []
    for i in arr1:
        arr_1.append(format(i, f"0{n}b"))   # n자리 2진수로 새로운 배열에 저장
    
    for i in arr2:
        arr_2.append(format(i, f"0{n}b"))   # n자리 2진수로 새로운 배열에 저장
    print(arr_1)
    print(arr_2)
    answer = []
    for i in range(n):
        result = []
        for j in range(n):
            if arr_1[i][j] == '1' or arr_2[i][j] == '1':
                result.append('#')
            elif arr_1[i][j] == '0' and arr_2[i][j] == '0':
                result.append(' ')

        answer.append(''.join(result))
    return answer

# n = 5
# arr1 = [9, 20, 28, 18, 11]
# arr2 = [30, 1, 21, 17, 28]
# 출력 : ["#####","# # #", "### #", "# ##", "#####"]

# result = solution(n, arr1, arr2)
# print(result)