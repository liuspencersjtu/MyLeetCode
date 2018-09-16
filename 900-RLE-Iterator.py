class RLEIterator:

    def __init__(self, A):
        """
        :type A: List[int]
        """
        self.rle = A

    def next(self, n):
        """
        :type n: int
        :rtype: int
        """
        while n>0:
            if self.rle == []:
                return -1
            if self.rle[0]>=n:
                self.rle[0] = self.rle[0] - n
                #print(self.rle)
                return self.rle[1]
                while self.rle and self.rle[0] == 0:
                    self.rle.pop(0)
                    self.rle.pop(0)
            else:
                n = n - self.rle[0]
                self.rle[0] = 0
                while self.rle and self.rle[0] == 0:
                    self.rle.pop(0)
                    self.rle.pop(0)
                
                
            
        


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)
