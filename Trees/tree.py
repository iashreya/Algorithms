class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None        
        
class BST:
    def __init__(self, root=None):
        self.root = root
        
    def insert(self, data):
        print("============ INSERTING NODE {0} ============".format(data))
        node = Node(data)
        
        if self.root == None:
            self.root = node
        else:
            temp = self.root
            while(True):
                if node.data <= temp.data:
                    if temp.left != None:
                        temp = temp.left
                    else:
                        temp.left = node
                        break
                else:
                    if temp.right != None:
                        temp = temp.right
                    else:
                        temp.right = node
                        break
                        
    def lookup(self, data):
        temp = self.root
        
        while(temp!=None):
            if temp.data == data:
                return temp
            elif data<temp.data:
                if temp.left != None:
                    temp = temp.left
                else:
                    return "Not Found"
            else:
                if temp.right != None:
                    temp = temp.right
                else:
                    return "Not Found" 
        return "Not Found"
    
    def remove(self, data):
        if self.root == None:
            return False
        else:
            currentNode = self.root
            parentNode = None
            
            while(currentNode):
                if data < currentNode.data:
                    parentNode = currentNode
                    currentNode = currentNode.left
                    
                    if currentNode == None:
                        return False
                    
                    if data == currentNode.data:
                        if currentNode.left == None and currentNode.right == None:
                            parentNode.left = None
                        elif currentNode.left == None and currentNode.right != None:
                            parentNode.left = currentNode.right
                        elif currentNode.left != None and currentNode.right == None:
                            parentNode.left = currentNode.left
                        else:
                            temp = currentNode.right
                            while(temp.left!=None):
                                temp = temp.left
                                
                            temp.left = currentNode.left
                            parentNode.left = temp
                            
                        currentNode = None
                        return True
                            
                    
                elif data > currentNode.data:
                    parentNode = currentNode
                    currentNode = currentNode.right
                    
                    if currentNode == None:
                        return False
                    
                    if data == currentNode.data:
                        if currentNode.left == None and currentNode.right == None:
                            parentNode.right = None
                        elif currentNode.left == None and currentNode.right != None:
                            parentNode.right = currentNode.right
                        elif currentNode.left != None and currentNode.right == None:
                            parentNode.right = currentNode.left
                        else:
                            temp = currentNode.right
                            while(temp.left!=None):
                                temp = temp.left
                                
                            temp.left = currentNode.left    
                            parentNode.right = temp
                            
                        currentNode = None
                        return True
        
    def height(self, node):
        if node!=None:
            l = self.height(node.left) + 1
            r = self.height(node.right) + 1

            if l>r:
                return l
            else:
                return r
        else:
            return 0
                    
    def traverse(self, node):
        if node!=None:
            self.traverse(node.left)
            print(node.data)
            self.traverse(node.right)
            
    def BFS(self, node):
        stack = [node]
        ans = []

        while(stack!=[]):
            temp = stack[0]
            del stack[0]
            ans.append(temp.data)

            if temp.left!=None:
                stack.append(temp.left)    
            if temp.right!=None:
                stack.append(temp.right)

        return ans
