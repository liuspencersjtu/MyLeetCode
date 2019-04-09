class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = []
        if not strs:
            return ''
        for i in range(len(strs[0])):
            curr = strs[0][i]
            for item in strs:
                if i>=len(item) or item[i] != curr:
                    return ''.join(res)
            res.append(curr)
        return ''.join(res)
