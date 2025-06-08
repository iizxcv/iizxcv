# 체인법으로 해시 함수 구현하기

from __future__ import annotations
from typing import Any, Type
import hashlib

class Node:
    """해시를 구성하는 함수"""
    
    
    def __init__(self, key:Any, value: Any, next: Node)-> None:
        """초기화"""
        self.key = key
        self.value = value
        self.next = next 
        
class ChainedHash:
    """체인법으로 해시 클래스 구현"""
    
    def __init__(self,capacity: int )-> None:
        """초기화"""
        self.capacity = capacity
        self.table = [None] * self.capacity
        
    def hash_value(self, key: Any) -> int:
        """해시값을 구함 """
        if isinstance(key,int):
            return key % self.capacity
        return(int(hashlib.sha256(str(key).encode().hexdigest(), 16)% self.capacity))
    
    def search(self,key : Any)-> Any:
        """키가 key인 원소를 검색하여 값을 반환"""
        
        hash= self.hash_value(key) #검색하느 키의 해시값
        p = self.table[hash] # 노드를 주목
        
        
        