import sys
sys.setrecursionlimit(10**6)

class Node():
    def __init__(self, data):
        self.data= data
        self.left = None
        self.right = None

class Binary_Tree():
    def __init__(self):
        self.root = None
        
    def add_Node(self, n):
        temp_node = Node(n)
        cur_tree = self.root
        
        
        while True:
            if cur_tree.data > temp_node.data and cur_tree.left :
                cur_tree = cur_tree.left
            
            elif cur_tree.data < temp_node.data and cur_tree.right:
                cur_tree = cur_tree.right
        
            elif cur_tree.data > temp_node.data and not cur_tree.left :
                cur_tree.left = temp_node
                break
            elif cur_tree.data < temp_node.data and not cur_tree.right:
                cur_tree.right = temp_node
                break
        
        return
    
    def preorder(self):
        stk = []
        stk.append((self.root, False))
        
        #while True:
        #temp,cf = stk.pop()
        #print(temp,cf)
        
        while stk:
            cur_node,cf = stk.pop()
            
            if cf:
                print(cur_node.data)
                continue
            
            stk.append((cur_node,True))
            if cur_node.right:
                stk.append((cur_node.right, False))
            if cur_node.left:
                stk.append((cur_node.left, False))

root_node = Node(int(input()))
n = Binary_Tree()
n.root= root_node
lst = list(map(int, sys.stdin.read().split()))
#print()
for _ in lst:
    n.add_Node(_)
n.preorder()

    