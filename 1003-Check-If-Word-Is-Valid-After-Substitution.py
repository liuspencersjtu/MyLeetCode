from collections import defaultdict
class Solution:
    def isValid(self, S: str) -> bool:
        memo = {'a':0,'b':0,'c':0}
        for i in S:
            memo[i]+=1
            if not (memo['a']>=memo['b']>=memo['c']):
                return False
        if memo['a']==memo['b'] and memo['b']==memo['c']:
            return True
        else:
            return False
            
