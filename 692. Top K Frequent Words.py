class Solution:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        memo = {}
        for item in words:
            if memo.get(item,0) == 0:
                memo[item] = 1
            else:
                memo[item] += 1
        #items = memo.items() 
        #items.sort() 
        memo_list = list(memo.items())
        def takeSecond(elem):
            return elem[1]
        def takeFirst(elem):
            return elem[0]
        memo_list.sort(key=takeFirst)
        memo_list.sort(key=takeSecond, reverse=True)
        return [i[0] for i in memo_list[:k]]