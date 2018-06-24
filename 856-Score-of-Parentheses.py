class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        # producer and consumer, somephore
        #stack = []
        temp = {}
        level = 0
        #score = 0
        s = list(S)
        if not s:
            return 0
        for i in s:
            if i == '(':                
                level += 1
                #stack.append(i)
                dirty = 0
            else:
                #if temp.get(level,0) == 0:
                #    temp[level] = 1
                #else:
                if dirty == 0:
                    if temp.get(level,0) == 0:
                        temp[level] = 1
                    else:
                        temp[level] += 1
                else:
                    if temp.get(level,0) == 0:
                        temp[level] = temp[level+1]*2
                    else:
                        temp[level] += temp[level+1]*2
                    temp[level+1] = 0
                level -= 1
                dirty = 1
        #print(temp)
        return temp[1]
        '''
        stack = []
        temp = 0
        dirty = 0
        score = 0
        s = list(S)
        for i in s:
            if i == '(':
                stack.append(i)
                dirty = 0
                print(temp,score,5,dirty)
            else:
                stack.pop()
                if stack:
                    if dirty == 0:
                        temp += 1
                        dirty = 1
                        print(temp,score,1,dirty)
                    else:
                        temp = temp*2
                        print(temp,score,2,dirty)
                else:
                    if temp == 0:
                        score += 1
                        print(temp,score,3,dirty)
                    else:
                        score += 2*temp
                        temp = 0
                        print(temp,score,4,dirty)
        return score
        '''