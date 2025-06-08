from my_max import max_of
"""내가 만든 max 함수 호출"""

print('배열의 최대값을 구합니다.')
num = int(input('원소 수를 입력하세요.: '))
x= [None] * num #원소 수가 num인 리스트 생성

for i in range(num):
    x[i] = int(input(f'x{i}값을 입력하세요'))
        
print (f'최대값은 {max_of(x)}')