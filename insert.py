class Node:#вершина
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class Tree:
    def __init__(self):
        self.root = None
    def __find(self, node, parent, value):
        if node is None:
            return None, parent, False
        if value == node.data:
            return node, parent, True
        
        if value < node.data:
            if node.left: #проверка на существование
                return self.__find(node.left, node, value)
        if value > node.data:
            if node.right: #проверка на существование
                return self.__find(node.right, node, value)
        return node, parent, False
    def append(self, obj):
        if self.root is None:
            self.root = obj
            return obj
        s, p, flag = self.__find(self.root, None, obj.data)
        if flag == False and s:
            if obj.data < s.data:
                s.left = obj
            else:
                s.right = obj
            return obj
    def show_tree(self, node):
        
        if node is None:
            return
        if node.right == node.left == None:
            answer.append(node.data)

        
             
        self.show_tree(node.left)
        
        self.show_tree(node.right)
        
    
str1 = list(map(int, input().split()))
str2 = list(map(int, input().split()))
tre = Tree()
answer = []
for i in str2:
    tre.append(Node(i))
tre.show_tree(tre.root)
