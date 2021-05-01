class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.N = 8
        self.cache = []
        self.stack = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if not self.cache:
            if len(self.stack)==self.N:
                self.cache.append([x])
            else:
                self.stack.append(x)
        else:
            if len(self.cache[-1])==self.N:
                self.cache.append([x])
            else:
                self.cache[-1].append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.stack:
            tmp = []
            while len(self.cache)>1:
                tmp.append(self.cache.pop())
            self.stack = self.cache.pop()
            while tmp:
                self.cache.append(tmp.pop())
        tmp = []
        while len(self.stack)>1:
            tmp.append(self.stack.pop())
        res = self.stack.pop()
        while tmp:
            self.stack.append(tmp.pop())
        return res
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.stack:
            tmp = []
            while len(self.cache)>1:
                tmp.append(self.cache.pop())
            self.stack = self.cache.pop()
            while tmp:
                self.cache.append(tmp.pop())
        tmp = []
        while len(self.stack)>1:
            tmp.append(self.stack.pop())
        res = self.stack.pop()
        tmp.append(res)
        while tmp:
            self.stack.append(tmp.pop())
        return res
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if not self.stack and not self.cache:
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
