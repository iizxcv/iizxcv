#z 재귀, 분할정복


N,c,r = map(int, input().split())
cnt = 0



ans = 0

while N != 0:

	N -= 1

	# 제2사분면
	if r < 2 ** N and c < 2 ** N:
		ans += ( 2 ** N ) * ( 2 ** N ) * 0

	# 제1사분면
	elif r < 2 ** N and c >= 2 ** N: 
		ans += ( 2 ** N ) * ( 2 ** N ) * 1
		c -= ( 2 ** N )
        
	# 제3사분면    
	elif r >= 2 ** N and c < 2 ** N: 
		ans += ( 2 ** N ) * ( 2 ** N ) * 2
		r -= ( 2 ** N )
        
	# 제4사분면    
	else:
		ans += ( 2 ** N ) * ( 2 ** N ) * 3
		r -= ( 2 ** N )
		c -= ( 2 ** N )
    
print(ans)


#print(cnt)   
#print(n,r,c)
 
 

      

    
    
'''
    if r >= 2**n and c < 2**n:
             z(n,r-(2**n-1),c)
    else: cnt += 2**n
    if r < 2**n and c >= 2**n:
         z(n,r,c(2**n-1))
    if r >= 2**n and c >= 2**n:
         z(n,r(2**n-1),c(2**n-1))
    '''
        



