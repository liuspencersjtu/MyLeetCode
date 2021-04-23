class Solution:
    def calculate(self, s: str) -> int:
        def compute(s : list):
            ## this compute only support nums and + - 
            if not s:
                return 0
            res = 0
            if s and s[0]=='-' or s[0]=='+':
                op = s.pop(0)
            else:
                op = '+'
            curr = []
            while s:
                if s[0]=='+' or s[0]=='-':
                    if op =='+':
                        res += int(''.join(curr))
                    elif op=='-':
                        res -= int(''.join(curr))
                    curr = []
                    op = s.pop(0)
                else:
                    curr.append(s.pop(0))
            if op =='+':
                res += int(''.join(curr))
            elif op=='-':
                res -= int(''.join(curr))
            return str(res)
            
        stack = []
        s = list(s)
        while s:
            if s[0] == ')':
                ## backwards until '('
                s.pop(0)
                tmp = []
                while stack[-1] != '(':
                    tmp.append(stack.pop())
                stack.pop() #pop (
                stack.append(compute(tmp[::-1]))
            elif s[0] == ' ':
                s.pop(0)
            else:
                stack.append(s.pop(0))
        return int(compute(stack))

# https://github.com/liuspencersjtu/awesome-algorithm/blob/master/docs/Leetcode_Solutions/Python/0224._Basic_Calculator.md
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        res, num, sign = 0, 0, 1
        for i, c in enumerate(s):
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in '+-':
                res += sign * num
                num = 0
                sign = 1 if c == '+' else -1
            elif c == '(': # push the result first, then sign;
                stack.append(res)
                stack.append(sign)
                res, sign = 0, 1 # reset the sign and res for the value in the parenthesis
            elif c == ')': # use elif because there may have space in input s
                res += sign * num # temporary res in this parenthesis
                num = 0
                res *= stack.pop() # sign before the left parenthesis
                res += stack.pop() # res calculated before the left parenthesis
        return res + sign * num
