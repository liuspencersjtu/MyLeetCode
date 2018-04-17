class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''
        def numberbreak(x):
            if x == 1:
                return [[1]]
            else:
                result = []
                for item in numberbreak(x-1):
                    if len(item)>1:
                        for i in range(len(item)):
                            newitem = list(item)
                            newitem[i] += 1
                            result.append(newitem)
                return [i+[1] for i in numberbreak(x-1)] + result
            
        combs = numberbreak(n)
        '''
        '''
        def numberbreak(x):
            if x == 2:
                return [[1,1]]
            else:
                result = []
                for item in numberbreak(x-1):
                    result.append(item+[1])
                    for i in range(len(item)):
                        newitem = list(item)
                        newitem[i] += 1
                        result.append(newitem)
                return result
            
        combs = numberbreak(n) 
        '''
        '''
        combs = [[1,1]]
        def numberbreak(x):
            nonlocal combs
            if x == n:
                pass
            else:
                newcomb=[]
                for item in combs:
                    newcomb.append(item+[1])
                    for i in range(len(item)):
                        newitem = list(item)
                        newitem[i] += 1
                        newcomb.append(newitem)
                combs = newcomb
                numberbreak(x+1)
        numberbreak(2)
        from functools import reduce
        return max([reduce(lambda x,y:x*y, item) for item in combs])
        '''
        if n == 2:
            return 1
        if n == 3:
            return 2
        list_3 = [3] * (n//3) # generate a list of 3
        mod_3 = n%3
        if mod_3 == 1: # if a 1 is left, then add it to the first element to get a 4
            list_3[0] += 1
        if mod_3 == 2: # if a 2 is left, then put it into the list
            list_3.append(2)
        from functools import reduce
        return reduce(lambda a, b: a*b, list_3)
    