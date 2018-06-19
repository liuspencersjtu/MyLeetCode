class Solution:
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        def func(nn, d):
            if nn==1:
                return 1
            ret = 1
            if d:
                ret = 2*func(nn//2, not d)
            else:
                if nn&1:
                    ret = 2*func(nn//2, not d)
                else:
                    ret = 2*func(nn//2, not d)-1
            return ret
        return func(n, True)
        '''
        num = [i for i in range(1,n+1)]
        fromleft = True
        def searchLeft(numbers):
            #return [numbers[i] for i in range(len(numbers)) if i%2==1]
            res = []
            i = 1
            n = len(numbers)
            while i < n:
                res.append(numbers[i])
                i += 2
            return res
        def searchRight(numbers):
            #numbers.reverse()
            #newNumbers = searchLeft(numbers)
            #newNumbers.reverse()
            #return newNumbers
            res = []
            i = len(numbers)-2
            while i >= 0:
                res.insert(0,numbers[i])
                i -= 2
            return res
        while len(num)>1:
            if fromleft:
                #num = searchLeft(num)
                res = []
                i = 1
                n = len(num)
                while i < n:
                    res.append(num[i])
                    i += 2
                num =  res
                fromleft = False
            else:
                #num = searchRight(num)
                res = []
                i = len(num)-2
                while i >= 0:
                    res.insert(0,num[i])
                    i -= 2
                num = res
                fromleft = True
        return num[0]
        '''