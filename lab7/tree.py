class node:   
    def __init__(self, data, left = None, right = None):     
        self.data = data     
        self.left = None if left is None else left     
        self.right = None if right is None else right 

    def __str__(self):     
        return str(self.data)  
    
    def getData(self):         # accessor     
        return self.data 
    
    def getLeft(self):         # accessor     
        return self.left 
    
    def getRight(self):        # accessor     
        return self.right 
    
    def setData(self, data):   # mutator     
        self.data = data 
    
    def setLeft(self, left):   # mutator     
        self.left = left 
    
    def setRight(self, right): # mutator     
        self.right = right 

class BST:     
    def __init__(self, root = None):         
        self.root = None if root is None else root 
    
    def addI(self, data):         
        if self.root is None:             
            self.root = node(data)         
        else:             
            fp = None       #father of p             
            p = self.root   #start comparing from root             
            while p:    # while p is not None                 
                fp = p                 
                p = p.left if data < p.data else p.right    # if data < p.data            
                                                            #    p = p.left              
                                                            # else:                  
                                                            #    p = p.right             
            if data < fp.data:                 
                fp.left = node(data)             
            else:                 
                fp.right = node(data) 
 
    def add(self, data):         
        self.root = BST._add(self.root, data) 
 
    def _add(root, data):   # recursive _add         
        if root is None:             
            return node(data)         
        else:             
            if data < root.data:                 
                root.left = BST._add(root.left, data)             
            else:                 
                root.right = BST._add(root.right, data)         
            return root      
            
    def inOrder(self):         
        BST._inOrder(self.root)         
        print() 
 
    def _inOrder(root):         
        if root:   # if root is not None             
            BST._inOrder(root.left)             
            print(root.data, end = ' ')             
            BST._inOrder(root.right) 
 
    def printSideway(self):         
        BST._printSideway(self.root, 0)         
        print() 
 
    def _printSideway(root, level):         
        if root :  # if root is not None             
            BST._printSideway(root.right, level+1)             
            print('   '*level, root.data, sep = '' )       
            BST._printSideway(root.left, level+1) 

    def preOrder(self): #พิมพ์ traverse ของ tree ในแต่ละแบบ 
        BST._preOrder(self.root)         
        print()

    def _preOrder(root):
        if root:   # if root is not None             
            print(root.data, end = ' ')             
            BST._inOrder(root.left)             
            BST._inOrder(root.right) 
    
    def postOrder(self): #พิมพ์ traverse ของ tree ในแต่ละแบบ 
        BST._postOrder(self.root)         
        print()

    def _postOrder(root):
        if root:   # if root is not None                          
            BST._inOrder(root.left)             
            BST._inOrder(root.right)
            print(root.data, end = ' ')

    def search(self, data):  # เพื่อหาว่ามี data อยู่ใน tree หรือไม่ return pointer ที่ชี้ไปที่ node นั้น (python : return node นั้น) หากมี หรือ return None หากไม่มี 
        if self.root is None:             
            return None         
        fp = None       #father of p             
        p = self.root   #start comparing from root 
        while p:    # while p is not None                 
            fp = p  
            if data == p.data:
                return p 
            elif data < p.data:  
                p = p.left              
            else:                  
                p = p.right 
        return None

    def path(self, data): #พิมพ์ path จาก root ไปยัง node ที่มีข้อมูล data 
        if self.root is None:             
            return
        fp = None       #father of p  
        l = []         
        p = self.root   #start comparing from root 
        while p:    # while p is not None                 
            fp = p  
            l.append(p.data)
            if data == p.data:
                s = ''
                for i in range(len(l)):
                    s += str(l[i])
                    if i is not len(l)-1:
                        s = s + ' -> '
                return s
            elif data < p.data:  
                p = p.left              
            else:                  
                p = p.right 
        return None
        

    def delete(self, data): #เพื่อ delete node ที่มีdata ออกจาก BST 
        return BST._delete(self.root, data)

    def _delete(root, data):
        if root is not None:
            if data < root.data:
                root.left = BST._delete(root.left, data)
            elif data > root.data:
                root.right = BST._delete(root.right, data)
            else:
                if root.left is None:
                    temp = root.right
                    root = None
                    return temp
                elif root.right is None:
                    temp = root.left
                    root = None
                    return temp

                temp = BST.minRoot(root.right)
                root.data = temp.data
                root.right = BST._delete(root.right, temp.data)
            return root

    def minRoot(root):
        cur = root
        # while cur.left is not None:
        #     cur = cur.left
        if cur.left is not None:
            cur = BST.minRoot(cur.left)
        return cur

l = [int(e) for e in input("insert integers : ").split()] 
print(l) 
 
t = BST() 
for ele in l:     
    t.addI(ele) 
 
t.inOrder() 
t.printSideway()
print(t.search(0))
print(t.path(17))
t.preOrder()
t.postOrder()
print(t.delete(21))
t.printSideway()