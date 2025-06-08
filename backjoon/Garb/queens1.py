n = int(input())
pos = [0] * n
flag_a = [False] * n            #flag_a 같은 col안에 퀸이 있는지 비교용 배열
flag_b = [False] * ((n * 2)-1)  #flag_b 대각선 우상단 비교용 배열
flag_c = [False] * ((n * 2)-1)  #flag_c 대각선 우하단 비교용 배열
count = 0

def put() -> None: #출력문
    global count
    #for i in range(n): #pos[0~n] 한줄 출력
        #for j in range(n):
        #print(f'{pos[i]:2}', end='')
    count+=1
            #print('◆' if pos[i]==j else '◇', end='' )
        #print()
    #print()
    
    
    
def set(i:int)-> None:
    
    for j in range(n):
        if (    not flag_a[j]                 # j반복에서 flag[j] 값이 False 가 아니면 == True
            and not flag_b[i+j]             # 
            and not flag_c[i-j + (n-1)]
            ):
            
            pos[i] = j  # 퀸을 체스 i 번째에 둠
            if i == n-1: #n

                put()
            else:
                
                flag_a[j] = flag_b[i + j] = flag_c[i - j + (n-1)] = True 
                set(i+1)
                flag_a[j] = flag_b[i + j] = flag_c[i - j + (n-1)] = False
                

set(0)
print(count)
    