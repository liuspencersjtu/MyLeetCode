class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        #remain = {item[0]:item[1] for item in enumerate(n*[")"]+(n-1)*["("])}
        remain = n*[")"]+(n-1)*["("]
        stack =["("]
        self.result = set()
        self.dfs("(", remain, stack)
        return list(self.result)
        
        
    def dfs(self, combs, remain, stack):
        if remain == []:
            self.result.add(combs)
        else:
            if ")" in remain:
                if stack != [] and stack[-1] == "(":
                    newremain = list(remain)
                    newremain.remove(")")
                    self.dfs(combs+")", newremain, stack[:-1])
            if "(" in remain:
                newremain = list(remain)
                newremain.remove("(")
                self.dfs(combs+"(", newremain, stack + ["("])
                
            """
            for i in range(len(remain)):#pruning
                if remain[i] ==")":
                    if stack != [] and stack[-1] == "(":
                        #stack.pop()
                        #newstack = stack[:-1]
                        #newcombs = combs+remain[i]
                        #newremain = remain[:i] if (i == len(remain) - 1) else (remain[:i]+ remain[i+1:])
                        #self.dfs(newcombs, newremain, newstack)
                        self.dfs(combs+remain[i], remain[:i]+ remain[i+1:], stack[:-1])
                else:
                    #newstack = stack + ["("]
                    #newcombs = combs+remain[i]
                    #newremain = remain[:i] if (i == len(remain) - 1) else (remain[:i]+ remain[i+1:])
                    #self.dfs(newcombs, newremain, newstack)
                    self.dfs(combs+remain[i], remain[:i]+ remain[i+1:], stack + ["("])
            """