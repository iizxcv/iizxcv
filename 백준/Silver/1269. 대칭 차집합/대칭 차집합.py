import sys

n,m = map(int,sys.stdin.readline().split());


s1 = set(sys.stdin.readline().split());
s2 = set(sys.stdin.readline().split());

result1 = s1-s2;
result2 = s2-s1;

result_cnt = len(result1) + len(result2)

print(result_cnt)
