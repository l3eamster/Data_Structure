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