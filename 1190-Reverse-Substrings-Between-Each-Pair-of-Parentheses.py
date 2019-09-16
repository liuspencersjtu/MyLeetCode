class Solution:
    def reverseParentheses(self, s: str) -> str:
        q = []
        p1, p2 = 0, 0
        N = len(s)
        for a in s:
            if a == ')':
                q2 = []
                while q[-1]!='(':
                    q2.append(q.pop()[::-1])
                q.pop()
                # if not q:
                    # return ''.join(q2)
                # else:
                q.append(''.join(q2))
            else:
                q.append(a)
        return ''.join(q)
