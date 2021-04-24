class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.N = 8
        self.storage = []
        self.queue = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        if len(self.queue) == self.N:
            self.storage.append(self.queue)
            self.queue = []
        self.queue.append(x)
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if not self.queue:
            newstorage = []
            M = len(self.storage)
            for i in range(0,M-1):
                newstorage.append(self.storage.pop(0))
            self.queue = self.storage.pop(0)
            self.storage = newstorage
        newqueue = []
        M = len(self.queue)
        for i in range(0,M-1):
            newqueue.append(self.queue.pop(0))
        res = self.queue.pop(0)
        self.queue = newqueue
        return res
        

    def top(self) -> int:
        """
        Get the top element.
        """
        if not self.queue:
            newstorage = []
            M = len(self.storage)
            for i in range(0,M-1):
                newstorage.append(self.storage.pop(0))
            self.queue = self.storage.pop(0)
            self.storage = newstorage
        newqueue = []
        M = len(self.queue)
        for i in range(0,M-1):
            newqueue.append(self.queue.pop(0))
        res = self.queue.pop(0)
        newqueue.append(res)
        self.queue = newqueue
        return res
        
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if not self.queue and not self.storage:
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
