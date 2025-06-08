#고정 길이 스택 클래스(fixeStack)을 사용하기

from enum import Enum
from stack import FixedStack

Menu = Enum('Menu', ['푸시','팝','피크','검색','덤프','종료'])

def select_menu() -> Menu:
    s = [f'({m.value}){m.name}' for m in Menu] 
    while True:
        print(*s, sep= ' ', end='')
        n = int(input(': '))
        if 1<= n <= len(Menu):
            return Menu(n)

stack = FixedStack(64)

while True:
    print(f'현재 데이터 개수: {len(stack)} / {stack.capacity}')
    selected = select_menu()
    if selected == Menu.푸시:
        x = input('데이터를 입력하세요:')
        try:
            stack.push(x)
        except FixedStack.Full:
            print('스택이 가득 차 있습니다.')
        
    elif selected == Menu.팝:
        try:
            x = stack.pop()
        except FixedStack.Empty:
            print('스택이 비어 있습니다.')
    
    elif selected == Menu.피크:
        try:
            x = stack.peek()
            print(f'피크한 데이터 {x}입니다.')
        except FixedStack.Empty:
            print('스택이 비어 있습니다.')
            
    elif selected == Menu.검색:
        x= int(input('검색할 값을 입력하세요:'))
        if x in stack:
            print(f'{stack.count(x)}개 포함되고, 맨 앞의 위치는 {stack.find(x)}입니다')
    
    elif selected == Menu.덤프:
        stack.dump()
    
    else:
        break
