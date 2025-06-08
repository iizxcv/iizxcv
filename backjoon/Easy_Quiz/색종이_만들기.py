import sys

def view_rectangle(size,sx,sy):        ## 현재 범위의 공간 탐색 및 view함수
    val = 0
    for i in range(sy,sy+size):        ##si+size인 이유: 인덱싱 방식에서 배열 끝범위를
        for j in range(sx,sx+size):    ## 단순 size로만 한다면 쪼개질때, 인덱스를 잘 못 불러올 수 있음
            val += paper[i][j] 
            #print(paper[i][j], end=' ')  
        #print()
    
    return val
        
def check_color_paper(size,sx,sy):
    global cnt1,cnt0
    si = size//2
    #if size == sum():
        #return 0
    sum1 = 0
    val = view_rectangle(size,sx,sy)
    # for _ in paper[sy:size][sx:size]:
    #   print(sum(_))
    # sum1 += sum(_)

    #print(sum1)
    if size*size == val:
        cnt1 +=1
    elif 0 == val:
        cnt0 +=1
     
    else:
        check_color_paper(si,sx,sy)                 #1사분면
        check_color_paper(si,sx+si,sy)              #2사분면
        check_color_paper(si,sx,sy+si)              #3사분면
        check_color_paper(si,sx+si,sy+si)           #4사분면
        
    return

    #print(sum(paper[sy:size-1][0]))
    #print(sum(a[sy:size-1][0]))


a =  int(sys.stdin.readline())

paper = []

for _ in range(0,a):
    paper.append(list(map(int,sys.stdin.readline().split(' '))))
    


cnt1=0
cnt0=0

check_color_paper(len(paper[0]),0,0)


print(cnt0)
print(cnt1)