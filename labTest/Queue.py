class Queue:
    def __init__(self, list = []):
        if list is None:
            self.items = []
        else:
            self.items = list

    def size(self):
        return len(self.items)

    def enQ(self, i);
        self.items.append(i)

    def deQ(self):
        if self.items is not None:
            return self.items.pop(0)