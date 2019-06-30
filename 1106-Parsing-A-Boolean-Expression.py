class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        if not expression:
            return False
        if expression == 't':
            return True
        if expression == 'f':
            return False
        if expression[0] == '!':
            new_expression = expression[2:len(expression)-1]
            return not self.parseBoolExpr(new_expression)
        if expression[0] == '&':
            stack = []
            res = True
            outer = True
            new_expression = expression[2:len(expression)-1]
            for i, it in enumerate(new_expression):
                if outer and it == 'f':
                    return False
                if it == '(':
                    if not stack:
                        outer  = False
                    stack.append(i)
                if it == ')':
                    loc = stack.pop()
                    if not stack:
                        #print(new_expression[loc+1:i],self.parseBoolExpr(new_expression[loc-1:i+1]))
                        res = res and self.parseBoolExpr(new_expression[loc-1:i+1])
                        outer = True
            return res
        if expression[0] == '|':
            stack = []
            res = False
            outer = True
            new_expression = expression[2:len(expression)-1]
            for i, it in enumerate(new_expression):
                if outer and it == 't':
                    return True
                if it == '(':
                    if not stack:
                        outer = False
                    stack.append(i)
                if it == ')':
                    loc = stack.pop()
                    if not stack:
                        #print(new_expression[loc+1:i],self.parseBoolExpr(new_expression[loc-1:i+1]))
                        res = res or self.parseBoolExpr(new_expression[loc-1:i+1])
                        outer  = True
            return res
