class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        # # raise tle error
        # res = []
        # for first, second in queries:
        #     val = bin(second ^ first)[2:]
        #     start = s.find(val)
        #     if start<0:
        #         res.append([-1,-1])
        #     else:
        #         res.append([start, start+len(val)-1])
        # return res
        
        # remember all of the possible queries
        from collections import defaultdict
        seen = {}
        for i in range(len(s)):
            if s[i]=='0':
                if 0 not in seen:
                    seen[0]=[i,i]
                continue
            val = 0
            for j in range(i,len(s)):
                val = val*2 + int(s[j])
                if val>2**32:
                    break # here do the trimming!!!
                else:
                    if val not in seen:
                        seen[val]=[i,j]
        res = []
        for first, second in queries:
            val = second^first
            if val in seen:
                res.append(seen[val])
            else:
                res.append([-1,-1])
        return res

                    

