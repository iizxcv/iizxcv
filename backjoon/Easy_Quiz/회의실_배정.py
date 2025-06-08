import sys

n = int(input())
cnt =0
last_end  = 0
room_times = []
for _ in range(n):
    s,d = (map(int,sys.stdin.readline().split()))
    room_times.append((d, s))

room_times.sort()
#print(room_times)

for end,start in room_times:
    if start >= last_end:
        cnt+=1
        last_end = end
            
#print(dp)
print(cnt)

    

