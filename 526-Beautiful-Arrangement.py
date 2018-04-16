class Solution:
    '''
    This will take 156ms
    '''
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        def search(place, nums):
            if place == 1:
                return 1
            else:
                return sum(search(place-1,nums-{item}) for item in nums if place%item == 0 or item%place == 0)
        return search(N,{i for i in range(1,N+1)})

'''
This will take ~1200ms
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        self.ways = 0
        self.length = N + 1
        nums = {i for i in range(N,0,-1)}
        #nums = [i+1 for i in range(N)]
        self.search(1, nums)
        return self.ways
        
        
    def search(self, place, nums):
        if place == self.length:
            self.ways += 1
        else:
            for item in nums:
                if place%item == 0 or item%place == 0:##pruning
                    #newnums = [ _ for _ in nums if _ != item]
                    self.search(place+1, nums - {item})
'''