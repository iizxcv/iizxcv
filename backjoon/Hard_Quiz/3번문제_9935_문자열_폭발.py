def explode_string(s, bomb):
    stack = []
    bomb_len = len(bomb)
    
    
    for char in s :
        # 스택에 쌓인 무자의 끝이 폭발 문자열과 같다면 제거
        stack.append(char)
        if len(stack)  >= bomb_len:
            if ''.join(stack[-bomb_len:]) == bomb:
                # 폭발 길이만큼 제거
                for _ in range(bomb_len):
                    stack.pop()
                    
    result = ''.join(stack)
    return result if result else "FRULA"

s = input().strip()
bomb = input().strip()

# 출력
print(explode_string(s,bomb))