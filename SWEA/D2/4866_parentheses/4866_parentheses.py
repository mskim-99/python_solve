T = int(input())

top = -1
size = 100
stack = ['0'] * size    # 사이즈 만큼의 배열 생성

def stack_push(item, size): # 스택 삽입 함수
    global top
    global ans
    top += 1
    if top == size:
        ans = -1
    else:   # 스택 사이즈 보다 작다면 현재 위치에 삽입
        stack[top] = item

def stack_pop():    # 스택 삭제 함수
    global top
    global ans
    if top == -1:
        ans = -1
    else:   # 스택이 비어있지 않다면 현재 위치 감소
        top -= 1

for tc in range(T):
    ans = -1
    sentence = list(input())

    for i in sentence:
        if i == '(':    # 여는 소괄호는 삽입
            stack_push('(', size)
        elif i == '{':  # 여는 중괄호는 삽입
            stack_push('{', size)
        elif i == ')':  # 닫는 소괄호 일 때
            if stack[top] == '(':   # 스택의 최상단이 '('이면 pop
                stack_pop()
        elif i == '}':  # 닫는 중괄호 일 때
            if stack[top] == '{':   # 스택의 최상단이 '}'이면 pop
                stack_pop()

    if top == -1:   # 스택이 비어 있다면 1반환
        ans = 1
    else:           # 스택이 비어 있지 않다면 0 반환
        ans = 0

    print(f"#{tc + 1} {ans}")