class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(s):
            count = collections.Counter(s)
            return count[min(s)]
        kqueries = [f(s) for s in queries]
        kwords = [f(s) for s in words]
        res = []
        for q in kqueries:
            res.append(len(list(filter(lambda x:x>q, kwords))))
        return res
