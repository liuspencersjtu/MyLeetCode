import math
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        import math
        stack = []
        op = set(['+','-','*','/'])
        def add(a,b):
            return a+b
        def minus(a,b):
            return a-b
        def mul(a,b):
            return a*b
        def div(a,b):
            if a*b>=0:
                return math.floor(a/b)
            else:
                print(a,b,math.ceil(a/b))
                return math.ceil(a/b)
            #return (abs(a)//abs(b))*b//abs(b)*a//abs(a)
        memo={'+':add,'-':minus,'*':mul,'/':div}
        for i in tokens:
            if i in op:
                b=stack.pop()
                a=stack.pop()
                #print(memo[i](a,b))
                stack.append(memo[i](a,b))
            else:
                stack.append(int(i))
        return int(stack[-1])
