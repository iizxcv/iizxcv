def permutation(arr, r):
    #1.
    arr = sorted(arr) # 받은 배열을 정렬렬
    used = [0 for _ in range(len(arr))] #배열의 크기만큼 사용 유무확인용 배열 생성성 
    
    def generate(chosen, used): # 실제 재귀적으로 수열 만드는 함수 chosen에 빈 리스트를 받아 채워넣는 형식
        #2.
        if len(chosen) == r: 
            print(chosen)
            return
        
        #3.
        for i in range(len(arr)):
            if not used[i]:
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen, used)
                used[i] = 0
                chosen.pop()
    generate([],used)
    
        
permutation('ABAC',4)
