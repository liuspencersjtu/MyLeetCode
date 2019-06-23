class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        total = sum(count)
        res = [0]*5
        res[-1] = float(count.index(max(count)))
        res[2] = float(sum([i*c for i,c in enumerate(count)])/total)
        for i,c in enumerate(count):
            if c!=0:
                res[0] = float(i)
                break
        for i,c in enumerate(count[::-1]):
            if c!=0:
                res[1] = float(255-i)
                break
        '''
        nums = list(enumerate(count))
        
        res[1] = float(sorted(nums, key=lambda x:x[1], reverse = True)[0][0])
        nums = list(enumerate(map(lambda x: float('inf') if x==0 else x, count)))
        res[0] = float(sorted(list(nums), key=lambda x:x[1])[0][0])
        '''
        if total%2==1:
            acc = 0
            for i,c in enumerate(count):
                acc += c
                if acc>total//2:
                    res[3] = float(i)
                    return res
        else:
            acc = 0
            for i,c in enumerate(count):
                acc += c
                if acc>total//2:
                    if res[3] == 0:
                        res[3] = float(i)
                        return res
                    else:
                        res[3] += float(i/2)
                        return res
                if acc == total//2:
                    res[3] = float(i/2)
                
