class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lst = []
        memo = collections.defaultdict(int)
        if len(s)==1 or len(s)==0:
            return len(s)
        lst.append(set(s[0]))
        res = 1
        last=set()
        for i in range(1,len(s)):
            if s[i] not in lst[i-1]:
                tmp = set(lst[i-1])
                tmp.add(s[i])
                lst.append(tmp)
                memo[s[i]]=i
                res = max(len(tmp),res)
            else:
                #tmp = lst[i-1]-lst[memo[s[i]]]
                tmp = set(s[memo[s[i]]:i])
                #print(lst[i-1],lst[memo[s[i]]])
                tmp.add(s[i])
                lst.append(tmp)
                memo[s[i]]=i
                res = max(len(tmp),res)
        #print(lst)
        return res
