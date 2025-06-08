import sys
from collections import deque
#sys.stdin = open('input.txt','r')

# NxN 크기 시험관
# 특정 위치 바이러스 존재 - 바이러스는 1 ~ k 까지 종류
# 모든 바이러스는 1초마다 상하좌우 ( 번호가 낮은 순서)
# S초가 지난 후에 바이러스 찾기

#  N K
# 시험관 정보
# -----
# S Y-1 X-1


direction=[(1,0),(-1,0),(0,1),(0,-1)]                             #상하좌우 탐색용
n,k = map(int, sys.stdin.readline().split())
flask = []                                                        #바이러스가 담길 플라스크
virus = [a for a in range(1,k+1)]                                 #k개의 바이러스
for _ in range(n):
    flask.append(list(map(int,sys.stdin.readline().split())))
s,py,px = map(int, sys.stdin.readline().split())
q = []                                                            # 순회용 리스트 생성


for y in range(n):
    for x in range(n):
        if flask[y][x] != 0:                                       # 바이러스 속성별로 정렬이 되어야 하기에 
            q.append((flask[y][x],0,y,x))                          # 바이러스,시간,좌표 순서 튜플로 저장
q.sort()                                                           # 우선순위 큐 느낌이 되어야 하기에 q정렬
q = deque(q)                                                       # q 자료형 deque로 설정정
 
while q:
    virus,time,cy,cx = q.popleft()
    if time == s:
        break
    for dy,dx in direction:                                         # 상하좌우를 반복문으로 꺼내기
        if 0 <= cy+dy < n and 0 <= cx+dx < n and flask[cy+dy][cx+dx] == 0: # 리스트 영역 안에 있고, 상하좌우가 0이면면
            flask[cy+dy][cx+dx] = virus                             # 현재 바이러스 속성을 2차원 리스트에 추가
            q.append((virus,time+1,cy+dy,cx+dx))                    # 큐에 바이러스 추가
    

    
print(flask[py-1][px-1])