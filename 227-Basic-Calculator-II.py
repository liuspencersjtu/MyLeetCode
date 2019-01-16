class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s += '+'
        curNum, sign, stack = 0, '+', []
        def mul(stack,y):
            a = stack.pop()
            stack.append([a[0],a[1]*y])
            return stack
        def div(stack,y):
            a = stack.pop()
            stack.append([a[0],a[1]//y])
            return stack
        operator = {'+': lambda stack, y: stack.append([1, y]),
                    '-': lambda stack, y: stack.append([-1, y]),
                    '*': mul,
                    '/': div}
        
                    #'*': lambda stack, y: stack.append([x*(y**i) for i, x in enumerate(stack.pop())]),
                    #'/': lambda stack, y: stack.append([x//(y**i) for i, x in enumerate(stack.pop())])}
        for curChar in s:
            if curChar.isdigit():
                curNum = curNum * 10 + int(curChar)
            if curChar in operator.keys():
                operator[sign](stack, curNum)
                sign, curNum = curChar, 0
        return(sum([x[0]*x[1] for x in stack]))
