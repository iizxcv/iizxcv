import sys
sys.stdin = open("input.txt",'r')

arr= [0]*11
arr= [1] = 1
arr = [2] = 2
arr = [3] = 4



def pibo_plus(n):

    
n = int(input())
nums = [0]*n


for _ in range(len(nums)):
    nums[_] = int(sys.stdin.readline())


for i in nums:
    print(pibo_plus(i))
    
