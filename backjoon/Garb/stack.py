#고정 길이 스택 클래스 구현

from typing import Any

class FixedStack:
    """고정 길이 스택 클래스"""
    
    class Empty(Exception):
        """비어있는 fixed stack에 팝 또는 피크할 때 내보내는 예외 처리"""
        pass
    
    class Full(Exception):
        """가득 찬 FixedStack에 푸시할 때 내보내는 예외 처리"""
        pass
    
    def __init__(self, capacity: int =256)-> None:
        """스택 초기화"""
        self.stk = [None]* capacity #스택 본체
        self.capacity = capacity
        self.ptr = 0
        
    def __len__(self) -> int:
        """스택에 쌓여 있는 데이터 개수를 반환"""
        return self.ptr
    
    def is_empty(self)-> bool:
        """스택이 비어 있는지 판단"""
        return self.ptr <= 0
    
    def is_full(self) -> bool:
        """스택이 가득차 있는지 판단"""
        return self.ptr >= self.capacity
    
    
    def push(self, value: Any)-> None:
        if self.is_full():
            raise FixedStack.Full
        self.stk[self.ptr] = value
        self.ptr +=1 
        
    def pop(self)-> Any:
        if self.is_empty():
            raise FixedStack.Empty
        self.ptr -= 1
        return self.stk[self.ptr]
    
    def peek(self) -> any:
        if self.is_empty():
            raise FixedStack.Empty
        return self.stk[self.ptr -1]
    
    def clear(self)-> None:
        self.ptr = 0
    
    
    
    def peek(self)-> Any:
        if self.is_empty():
            raise FixedStack.Empty
        return self.stk[self.ptr -1]
    
    def find(self, value: Any) -> Any:
        """스택에서 value를 찾아 인덱스를 반환(없으면 -1을) 반환"""
        for i in range(self.ptr - 1,-1 -1):
            if self.stk[i] == value:
                return i
        return
    
    def count(self, value: Any)-> int:
        """스택에 있는 value의 개수를 반환"""
        c = 0
        for i in range(self.ptr):
            if self.stk[i] == value:
                c += 1
        return c
    
    def __contains__(self, value:Any)-> bool:
        """스택에 value가 있는지 판단"""
        
        return self.count(value) > 0
    
    def dump(self) -> None:
        """덤프(스택 안의 모든 데이터를 바닥부터 꼭대기 순으로 출력)"""
        if self.is_empty():
            print("스텍이 비어 있습니다.")
        else:
            print(self.stk[:self.ptr])
    
    