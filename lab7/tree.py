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

    # def preOrder(self): 
    
    # def postOrder(self):

    # def search(self, data):  

    # def path(self, data):

    # def del(self, data):

l = [int(e) for e in input("insert integers : ").split()] 
print(l) 
 
t = BST() 
for ele in l:     
    t.addI(ele) 
 
t.inOrder() 
t.printSideway()