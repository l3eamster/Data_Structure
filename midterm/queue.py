class Queue:

    def __init__(self, queue = None, n = 10):
        self.n = n
        if(queue == None):
            self.queue = []
        elif type(queue) is str:
            self.queue = list(queue)
        else:    
            self.queue = queue

    def enQueue(self, item):
        self.queue.append(item)
    
    def deQueue(self):
        if len(self.queue) != 0:
            return self.queue.pop(0)

    def isEmpty(self):
        return self.queue == []

    def isFull(self):
         return len(self.queue) == n
    
    def size(self):
        return len(self.queue)

#ENCODE DATA
def encode(data):
    keys = Queue([2,5,6,1,8,3])
    encodedData = Queue()
    while not data.isEmpty():
        asci = ord(data.deQueue())
        if asci != 32:
            key = keys.deQueue()
            asci += key
            keys.enQueue(key)
            if (asci > ord('Z') and asci < ord('a')) or (asci > ord('z')):
                asci -= 26
        encodedData.enQueue(chr(asci))
    return encodedData

# def encode(data):
#     keys = Queue([2,5,6,1,8,3])
#     encodedData = Queue()
#     while(not data.isEmpty()):        
#         asci = ord(data.deQueue())
#         if asci != 32:
#             key = keys.deQueue()
#             asci += key
#             keys.enQueue(key)
#             if (asci > ord('Z') and asci < ord('a')) or (asci > ord('z')):
#                 asci -= 26
#         encodedData.enQueue(chr(asci))
#     return encodedData
    
#DECODE DATA

def decode(data):
    keys = Queue([2,5,6,1,8,3])
    decodedData = Queue()
    while not data.isEmpty():
        asci = ord(data.deQueue())
        if asci != 32:
            key = keys.deQueue()
            asci -= key
            keys.enQueue(key)
            if (asci < ord('A')) or (asci < ord('a') and asci > ord('Z')):
                asci+=26
        decodedData.enQueue(chr(asci))
    return decodedData

# def decode(data):
#     keys = Queue([2,5,6,1,8,3])
#     decodedData = Queue()
#     while(not data.isEmpty()):        
#         asci = ord(data.deQueue())
#         if asci != 32:
#             key = keys.deQueue()
#             asci -= key
#             keys.enQueue(key)
#             if (asci < ord('A')) or (asci < ord('a') and asci > ord('Z')):
#                 asci += 26
#         decodedData.enQueue(chr(asci))
#     return decodedData

def list_to_str(data):
    str = ''
    for s in data:
        str += s
    return str

data = Queue('I Love Python')

data = encode(data)
print(list_to_str(data.queue))

data = decode(data)
print(list_to_str(data.queue))
